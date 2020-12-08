import * as docker from "@pulumi/docker";
import * as pulumi from "@pulumi/pulumi";

// Fetch the Docker Hub auth info from config.
const config = new pulumi.Config();
const username = config.require("dockerUsername");
const password = config.requireSecret("dockerPassword");

// Populate the registry info (creds and endpoint).
const imageName = `${username}/myapp`;
const registryInfo = {
    server: "docker.io",
    username: username,
    password: password,
};

// Build and publish the container image.
const image = new docker.Image("my-image", {
    build: "app",
    imageName: imageName,
    registry: registryInfo,
});

// Export the resuling base name in addition to the specific version pushed.
export const baseImageName = image.baseImageName;
export const fullImageName = image.imageName;
