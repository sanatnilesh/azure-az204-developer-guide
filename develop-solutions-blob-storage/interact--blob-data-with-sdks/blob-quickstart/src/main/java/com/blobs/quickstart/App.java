package com.blobs.quickstart;

/**
 * Azure Blob Storage quickstart
 */
import com.azure.identity.*;
import com.azure.storage.blob.*;
import com.azure.storage.blob.models.*;
import java.io.*;

public class App {
    public static void main(String[] args) {

        /*
         * The default credential first checks environment variables for configuration
         * If environment configuration is incomplete, it will try managed identity
         */
        DefaultAzureCredential defaultCredential = new DefaultAzureCredentialBuilder().build();

        // Azure SDK client builders accept the credential as a parameter
        // TODO: Replace <storage-account-name> with your actual storage account name
        BlobServiceClient blobServiceClient = new BlobServiceClientBuilder()
                .endpoint("https://blobstoragesanat.blob.core.windows.net/")
                .credential(defaultCredential)
                .buildClient();

        // Create a unique name for the container
        String containerName = "quickstartblobsbysanat" + java.util.UUID.randomUUID();

        // Create the container and return a container client object
        BlobContainerClient blobContainerClient = blobServiceClient.createBlobContainer(containerName);

        // Create the ./data/ directory and a file for uploading and downloading
        String localPath = "./data/";
        new File(localPath).mkdirs();
        String fileName = "quickstart" + java.util.UUID.randomUUID() + ".txt";

        // Get a reference to a blob
        BlobClient blobClient = blobContainerClient.getBlobClient(fileName);

        // Write text to the file
        FileWriter writer = null;
        try {
            writer = new FileWriter(localPath + fileName, true);
            writer.write("Hello, World!");
            writer.close();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

        System.out.println("\nUploading to Blob storage as blob:\n\t" + blobClient.getBlobUrl());

        // Upload the blob
        blobClient.uploadFromFile(localPath + fileName);

        System.out.println("\nListing blobs...");

        // List the blob(s) in the container.
        for (BlobItem blobItem : blobContainerClient.listBlobs()) {
            System.out.println("\t" + blobItem.getName());
        }

        // Download the blob to a local file

        // Append the string "DOWNLOAD" before the .txt extension for comparison
        // purposes
        String downloadFileName = fileName.replace(".txt", "DOWNLOAD.txt");

        System.out.println("\nDownloading blob to\n\t " + localPath + downloadFileName);

        blobClient.downloadToFile(localPath + downloadFileName);

    }
}
