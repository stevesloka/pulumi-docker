// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface ContainerCapabilities {
    /**
     * list of linux capabilities to add.
     */
    adds?: string[];
    /**
     * list of linux capabilities to drop.
     */
    drops?: string[];
}

export interface ContainerDevice {
    /**
     * The path in the container where the
     * device will be binded.
     */
    containerPath?: string;
    /**
     * The path on the host where the device
     * is located.
     */
    hostPath: string;
    /**
     * The cgroup permissions given to the
     * container to access the device.
     * Defaults to `rwm`.
     */
    permissions?: string;
}

export interface ContainerHealthcheck {
    /**
     * Time between running the check `(ms|s|m|h)`. Default: `0s`.
     */
    interval?: string;
    /**
     * Consecutive failures needed to report unhealthy. Default: `0`.
     */
    retries?: number;
    /**
     * Start period for the container to initialize before counting retries towards unstable `(ms|s|m|h)`. Default: `0s`.
     */
    startPeriod?: string;
    /**
     * Command to run to check health. For example, to run `curl -f http://localhost/health` set the
     * command to be `["CMD", "curl", "-f", "http://localhost/health"]`.
     */
    tests: string[];
    /**
     * Maximum time to allow one check to run `(ms|s|m|h)`. Default: `0s`.
     */
    timeout?: string;
}

export interface ContainerHost {
    /**
     * Hostname to add.
     */
    host: string;
    /**
     * IP address this hostname should resolve to.
     */
    ip: string;
}

export interface ContainerLabel {
    /**
     * Name of the label
     */
    label: string;
    /**
     * Value of the label
     */
    value: string;
}

export interface ContainerMount {
    /**
     * Optional configuration for the `bind` type.
     */
    bindOptions?: outputs.ContainerMountBindOptions;
    /**
     * If true, this volume will be readonly.
     * Defaults to false.
     */
    readOnly?: boolean;
    /**
     * The mount source (e.g., a volume name, a host path)
     */
    source?: string;
    /**
     * The container path.
     */
    target: string;
    /**
     * Optional configuration for the `tmpf` type.
     */
    tmpfsOptions?: outputs.ContainerMountTmpfsOptions;
    /**
     * The mount type: valid values are `bind|volume|tmpfs`.
     */
    type: string;
    /**
     * Optional configuration for the `volume` type.
     */
    volumeOptions?: outputs.ContainerMountVolumeOptions;
}

export interface ContainerMountBindOptions {
    /**
     * A propagation mode with the value.
     */
    propagation?: string;
}

export interface ContainerMountTmpfsOptions {
    /**
     * The permission mode for the tmpfs mount in an integer.
     */
    mode?: number;
    /**
     * The size for the tmpfs mount in bytes.
     */
    sizeBytes?: number;
}

export interface ContainerMountVolumeOptions {
    driverName?: string;
    /**
     * Options for the driver.
     */
    driverOptions?: {[key: string]: string};
    /**
     * Adding labels.
     */
    labels?: outputs.ContainerMountVolumeOptionsLabel[];
    /**
     * Whether to populate volume with data from the target.
     */
    noCopy?: boolean;
}

export interface ContainerMountVolumeOptionsLabel {
    /**
     * Name of the label
     */
    label: string;
    /**
     * Value of the label
     */
    value: string;
}

export interface ContainerNetworkData {
    /**
     * *Deprecated:* Use `networkData` instead. The network gateway of the container as read from its
     * NetworkSettings.
     */
    gateway: string;
    /**
     * *Deprecated:* Use `networkData` instead. The IP address of the container's first network it.
     */
    ipAddress: string;
    /**
     * *Deprecated:* Use `networkData` instead. The IP prefix length of the container as read from its
     * NetworkSettings.
     */
    ipPrefixLength: number;
    networkName: string;
}

export interface ContainerNetworksAdvanced {
    /**
     * The network aliases of the container in the specific network.
     */
    aliases?: string[];
    /**
     * The IPV4 address of the container in the specific network.
     */
    ipv4Address?: string;
    /**
     * The IPV6 address of the container in the specific network.
     */
    ipv6Address?: string;
    /**
     * The name of the network.
     */
    name: string;
}

export interface ContainerPort {
    /**
     * Port exposed out of the container. If not given a free random port `>= 32768` will be used.
     */
    external: number;
    /**
     * Port within the container.
     */
    internal: number;
    /**
     * IP address this hostname should resolve to.
     */
    ip?: string;
    /**
     * Protocol that can be used over this port,
     * defaults to `tcp`.
     */
    protocol?: string;
}

export interface ContainerUlimit {
    hard: number;
    name: string;
    soft: number;
}

export interface ContainerUpload {
    /**
     * Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.
     */
    content?: string;
    contentBase64?: string;
    /**
     * If true, the file will be uploaded with user
     * executable permission.
     * Defaults to false.
     */
    executable?: boolean;
    /**
     * path to a file in the container.
     */
    file: string;
    /**
     * A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state.
     */
    source?: string;
    /**
     * If using `source`, this will force an update if the file content has updated but the filename has not. 
     */
    sourceHash?: string;
}

export interface ContainerVolume {
    /**
     * The path in the container where the
     * device will be binded.
     */
    containerPath?: string;
    /**
     * The container where the volume is
     * coming from.
     */
    fromContainer?: string;
    /**
     * The path on the host where the device
     * is located.
     */
    hostPath?: string;
    /**
     * If true, this volume will be readonly.
     * Defaults to false.
     */
    readOnly?: boolean;
    /**
     * The name of the docker volume which
     * should be mounted.
     */
    volumeName?: string;
}

export interface GetNetworkIpamConfig {
    auxAddress?: {[key: string]: any};
    gateway?: string;
    ipRange?: string;
    subnet?: string;
}

export interface NetworkIpamConfig {
    auxAddress?: {[key: string]: any};
    gateway?: string;
    ipRange?: string;
    subnet?: string;
}

export interface NetworkLabel {
    /**
     * Name of the label
     */
    label: string;
    /**
     * Value of the label
     */
    value: string;
}

export interface ProviderRegistryAuth {
    address?: string;
    configFile?: string;
    configFileContent?: string;
    password?: string;
    username?: string;
}

export interface SecretLabel {
    /**
     * Name of the label
     */
    label: string;
    /**
     * Value of the label
     */
    value: string;
}

export interface ServiceAuth {
    /**
     * The password to use for authenticating to the registry. If this is blank, the `DOCKER_REGISTRY_PASS` is also be checked.
     */
    password?: string;
    /**
     * The address of the registry server
     */
    serverAddress: string;
    /**
     * The username to use for authenticating to the registry. If this is blank, the `DOCKER_REGISTRY_USER` is also be checked. 
     */
    username?: string;
}

export interface ServiceConvergeConfig {
    /**
     * Time between each the check to check docker endpoint `(ms|s|m|h)`. For example, to check if
     * all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: `7s`.
     */
    delay?: string;
    /**
     * The timeout of the service to reach the desired state `(s|m)`. Default: `3m`.
     */
    timeout?: string;
}

export interface ServiceEndpointSpec {
    /**
     * The mode of resolution to use for internal load balancing between tasks. `(vip|dnsrr)`. Default: `vip`.
     */
    mode: string;
    /**
     * See Ports below for details.
     */
    ports?: outputs.ServiceEndpointSpecPort[];
}

export interface ServiceEndpointSpecPort {
    /**
     * The name of the Docker service.
     */
    name?: string;
    /**
     * Protocol that can be used over this port: `tcp|udp|sctp`. Default: `tcp`.
     */
    protocol?: string;
    /**
     * Represents the mode in which the port is to be published: `ingress|host`
     */
    publishMode?: string;
    /**
     * The port on the swarm hosts. If not set the value of `targetPort` will be used.
     */
    publishedPort: number;
    /**
     * Port inside the container.
     */
    targetPort: number;
}

export interface ServiceLabel {
    /**
     * Name of the label
     */
    label: string;
    /**
     * Value of the label
     */
    value: string;
}

export interface ServiceMode {
    /**
     * set it to `true` to run the service in the global mode
     */
    global?: boolean;
    /**
     * , which contains atm only the amount of `replicas`
     */
    replicated: outputs.ServiceModeReplicated;
}

export interface ServiceModeReplicated {
    replicas?: number;
}

export interface ServiceRollbackConfig {
    /**
     * Delay between restart attempts `(ms|s|m|h)`
     * all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: `7s`.
     */
    delay?: string;
    /**
     * Action on update failure: `pause|continue|rollback`.
     */
    failureAction?: string;
    /**
     * The failure rate to tolerate during an update as `float`. **Important:** the `float`need to be wrapped in a `string` to avoid internal
     * casting and precision errors.
     */
    maxFailureRatio?: string;
    /**
     * Duration after each task update to monitor for failure `(ns|us|ms|s|m|h)`
     */
    monitor?: string;
    /**
     * Update order either 'stop-first' or 'start-first'.
     */
    order?: string;
    /**
     * The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).
     */
    parallelism?: number;
}

export interface ServiceTaskSpec {
    /**
     * See ContainerSpec below for details.
     */
    containerSpec: outputs.ServiceTaskSpecContainerSpec;
    /**
     * A counter that triggers an update even if no relevant parameters have been changed. See [Docker Spec](https://github.com/docker/swarmkit/blob/master/api/specs.proto#L126).
     */
    forceUpdate: number;
    /**
     * See Log Driver below for details.
     */
    logDriver?: outputs.ServiceTaskSpecLogDriver;
    /**
     * Ids of the networks in which the container will be put in.
     */
    networks?: string[];
    /**
     * See Placement below for details.
     */
    placement: outputs.ServiceTaskSpecPlacement;
    /**
     * See Resources below for details.
     */
    resources: outputs.ServiceTaskSpecResources;
    /**
     * See Restart Policy below for details.
     */
    restartPolicy: outputs.ServiceTaskSpecRestartPolicy;
    /**
     * Runtime is the type of runtime specified for the task executor. See [Docker Runtime](https://github.com/moby/moby/blob/master/api/types/swarm/runtime.go).
     */
    runtime: string;
}

export interface ServiceTaskSpecContainerSpec {
    /**
     * Arguments to the command.
     */
    args?: string[];
    /**
     * The command to be run in the image.
     */
    commands?: string[];
    /**
     * See Configs below for details.
     */
    configs?: outputs.ServiceTaskSpecContainerSpecConfig[];
    /**
     * The working directory for commands to run in.
     */
    dir?: string;
    /**
     * See DNS Config below for details.
     */
    dnsConfig: outputs.ServiceTaskSpecContainerSpecDnsConfig;
    /**
     * A list of environment variables in the form VAR=value.
     */
    env?: {[key: string]: string};
    /**
     * A list of additional groups that the container process will run as.
     */
    groups?: string[];
    /**
     * See Healthcheck below for details.
     */
    healthcheck: outputs.ServiceTaskSpecContainerSpecHealthcheck;
    /**
     * The hostname to use for the container, as a valid RFC 1123 hostname.
     */
    hostname?: string;
    hosts?: outputs.ServiceTaskSpecContainerSpecHost[];
    /**
     * The image used to create the Docker service.
     */
    image: string;
    /**
     * Isolation technology of the containers running the service. (Windows only). Valid values are: `default|process|hyperv`
     */
    isolation?: string;
    /**
     * See Labels below for details.
     */
    labels?: outputs.ServiceTaskSpecContainerSpecLabel[];
    /**
     * See Mounts below for details.
     */
    mounts?: outputs.ServiceTaskSpecContainerSpecMount[];
    /**
     * See Privileges below for details.
     */
    privileges?: outputs.ServiceTaskSpecContainerSpecPrivileges;
    /**
     * Mount the container's root filesystem as read only.
     */
    readOnly?: boolean;
    /**
     * See Secrets below for details.
     */
    secrets?: outputs.ServiceTaskSpecContainerSpecSecret[];
    /**
     * Amount of time to wait for the container to terminate before forcefully removing it `(ms|s|m|h)`.
     */
    stopGracePeriod: string;
    /**
     * Signal to stop the container.
     */
    stopSignal?: string;
    /**
     * The user inside the container.
     */
    user?: string;
}

export interface ServiceTaskSpecContainerSpecConfig {
    /**
     * ConfigID represents the ID of the specific config.
     */
    configId: string;
    /**
     * The name of the config that this references, but internally it is just provided for lookup/display purposes
     */
    configName?: string;
    /**
     * Represents the file GID. Defaults: `0`
     */
    fileGid?: string;
    /**
     * Represents the FileMode of the file. Defaults: `0444`
     */
    fileMode?: number;
    /**
     * Represents the final filename in the filesystem. The specific target file that the config data is written within the docker container, e.g. `/root/config/config.json`
     */
    fileName: string;
    /**
     * Represents the file UID. Defaults: `0`
     */
    fileUid?: string;
}

export interface ServiceTaskSpecContainerSpecDnsConfig {
    /**
     * The IP addresses of the name servers, for example, `8.8.8.8`
     */
    nameservers: string[];
    /**
     * A list of internal resolver variables to be modified, for example, `debug`, `ndots:3`
     */
    options?: string[];
    /**
     * A search list for host-name lookup.
     */
    searches?: string[];
}

export interface ServiceTaskSpecContainerSpecHealthcheck {
    /**
     * Time between running the check `(ms|s|m|h)`. Default: `0s`.
     */
    interval?: string;
    /**
     * Consecutive failures needed to report unhealthy. Default: `0`.
     */
    retries?: number;
    /**
     * Start period for the container to initialize before counting retries towards unstable `(ms|s|m|h)`. Default: `0s`.
     */
    startPeriod?: string;
    /**
     * Command to run to check health. For example, to run `curl -f http://localhost/health` set the
     * command to be `["CMD", "curl", "-f", "http://localhost/health"]`.
     */
    tests: string[];
    /**
     * Maximum time to allow one check to run `(ms|s|m|h)`. Default: `0s`.
     */
    timeout?: string;
}

export interface ServiceTaskSpecContainerSpecHost {
    /**
     * A list of hostname/IP mappings to add to the container's hosts file.
     */
    host: string;
    /**
     * The ip
     */
    ip: string;
}

export interface ServiceTaskSpecContainerSpecLabel {
    /**
     * Name of the label
     */
    label: string;
    /**
     * Value of the label
     */
    value: string;
}

export interface ServiceTaskSpecContainerSpecMount {
    /**
     * Optional configuration for the `bind` type.
     */
    bindOptions?: outputs.ServiceTaskSpecContainerSpecMountBindOptions;
    /**
     * Mount the container's root filesystem as read only.
     */
    readOnly?: boolean;
    /**
     * The mount source (e.g., a volume name, a host path)
     */
    source?: string;
    /**
     * The container path.
     */
    target: string;
    /**
     * Optional configuration for the `tmpf` type.
     */
    tmpfsOptions?: outputs.ServiceTaskSpecContainerSpecMountTmpfsOptions;
    /**
     * SELinux type label
     */
    type: string;
    /**
     * Optional configuration for the `volume` type.
     */
    volumeOptions?: outputs.ServiceTaskSpecContainerSpecMountVolumeOptions;
}

export interface ServiceTaskSpecContainerSpecMountBindOptions {
    /**
     * A propagation mode with the value.
     */
    propagation?: string;
}

export interface ServiceTaskSpecContainerSpecMountTmpfsOptions {
    /**
     * See Mode below for details.
     */
    mode?: number;
    /**
     * The size for the tmpfs mount in bytes. 
     */
    sizeBytes?: number;
}

export interface ServiceTaskSpecContainerSpecMountVolumeOptions {
    driverName?: string;
    driverOptions?: {[key: string]: string};
    /**
     * See Labels below for details.
     */
    labels?: outputs.ServiceTaskSpecContainerSpecMountVolumeOptionsLabel[];
    /**
     * Whether to populate volume with data from the target.
     */
    noCopy?: boolean;
}

export interface ServiceTaskSpecContainerSpecMountVolumeOptionsLabel {
    /**
     * Name of the label
     */
    label: string;
    /**
     * Value of the label
     */
    value: string;
}

export interface ServiceTaskSpecContainerSpecPrivileges {
    /**
     * For managed service account (Windows only)
     */
    credentialSpec?: outputs.ServiceTaskSpecContainerSpecPrivilegesCredentialSpec;
    /**
     * SELinux labels of the container
     */
    seLinuxContext?: outputs.ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext;
}

export interface ServiceTaskSpecContainerSpecPrivilegesCredentialSpec {
    /**
     * Load credential spec from this file.
     */
    file?: string;
    /**
     * Load credential spec from this value in the Windows registry.
     */
    registry?: string;
}

export interface ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext {
    /**
     * Disable SELinux
     */
    disable?: boolean;
    /**
     * SELinux level label
     */
    level?: string;
    /**
     * SELinux role label
     */
    role?: string;
    /**
     * SELinux type label
     */
    type?: string;
    /**
     * The user inside the container.
     */
    user?: string;
}

export interface ServiceTaskSpecContainerSpecSecret {
    /**
     * Represents the file GID. Defaults: `0`
     */
    fileGid?: string;
    /**
     * Represents the FileMode of the file. Defaults: `0444`
     */
    fileMode?: number;
    /**
     * Represents the final filename in the filesystem. The specific target file that the secret data is written within the docker container, e.g. `/root/secret/secret.json`
     */
    fileName: string;
    /**
     * Represents the file UID. Defaults: `0`
     */
    fileUid?: string;
    /**
     * ConfigID represents the ID of the specific secret.
     */
    secretId: string;
    /**
     * The name of the secret that this references, but internally it is just provided for lookup/display purposes
     */
    secretName?: string;
}

export interface ServiceTaskSpecLogDriver {
    /**
     * The logging driver to use. Either `(none|json-file|syslog|journald|gelf|fluentd|awslogs|splunk|etwlogs|gcplogs)`.
     */
    name: string;
    /**
     * The options for the logging driver, e.g.
     */
    options?: {[key: string]: string};
}

export interface ServiceTaskSpecPlacement {
    /**
     * An array of constraints. e.g.: `node.role==manager`
     */
    constraints?: string[];
    /**
     * Platforms stores all the platforms that the service's image can run on
     */
    platforms?: outputs.ServiceTaskSpecPlacementPlatform[];
    /**
     * Preferences provide a way to make the scheduler aware of factors such as topology. They are provided in order from highest to lowest precedence, e.g.: `spread=node.role.manager`
     */
    prefs?: string[];
}

export interface ServiceTaskSpecPlacementPlatform {
    /**
     * The architecture, e.g., `amd64`
     */
    architecture: string;
    /**
     * The operation system, e.g., `linux`
     */
    os: string;
}

export interface ServiceTaskSpecResources {
    /**
     * Describes the resources which can be advertised by a node and requested by a task.
     */
    limits?: outputs.ServiceTaskSpecResourcesLimits;
    /**
     * An object describing the resources which can be advertised by a node and requested by a task.
     */
    reservation?: outputs.ServiceTaskSpecResourcesReservation;
}

export interface ServiceTaskSpecResourcesLimits {
    /**
     * User-defined resources can be either Integer resources (e.g, SSD=3) or String resources (e.g, GPU=UUID1)
     */
    genericResources?: outputs.ServiceTaskSpecResourcesLimitsGenericResources;
    /**
     * The amount of memory in bytes the container allocates
     */
    memoryBytes?: number;
    /**
     * CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least 1000000
     */
    nanoCpus?: number;
}

export interface ServiceTaskSpecResourcesLimitsGenericResources {
    /**
     * The Integer resources, delimited by `=`
     */
    discreteResourcesSpecs?: string[];
    /**
     * The String resources, delimited by `=`
     */
    namedResourcesSpecs?: string[];
}

export interface ServiceTaskSpecResourcesReservation {
    /**
     * User-defined resources can be either Integer resources (e.g, SSD=3) or String resources (e.g, GPU=UUID1)
     */
    genericResources?: outputs.ServiceTaskSpecResourcesReservationGenericResources;
    /**
     * The amount of memory in bytes the container allocates
     */
    memoryBytes?: number;
    /**
     * CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least 1000000
     */
    nanoCpus?: number;
}

export interface ServiceTaskSpecResourcesReservationGenericResources {
    /**
     * The Integer resources, delimited by `=`
     */
    discreteResourcesSpecs?: string[];
    /**
     * The String resources, delimited by `=`
     */
    namedResourcesSpecs?: string[];
}

export interface ServiceTaskSpecRestartPolicy {
    /**
     * Condition for restart: `(none|on-failure|any)`
     */
    condition?: string;
    /**
     * Delay between restart attempts `(ms|s|m|h)`
     */
    delay?: string;
    /**
     * Maximum attempts to restart a given container before giving up (default value is `0`, which is ignored)
     */
    maxAttempts?: number;
    /**
     * The time window used to evaluate the restart policy (default value is `0`, which is unbounded) `(ms|s|m|h)`
     */
    window?: string;
}

export interface ServiceUpdateConfig {
    /**
     * Delay between updates `(ns|us|ms|s|m|h)`, e.g. `5s`.
     */
    delay?: string;
    /**
     * Action on update failure: `pause|continue|rollback`.
     */
    failureAction?: string;
    /**
     * The failure rate to tolerate during an update as `float`. **Important:** the `float`need to be wrapped in a `string` to avoid internal
     * casting and precision errors.
     */
    maxFailureRatio?: string;
    /**
     * Duration after each task update to monitor for failure `(ns|us|ms|s|m|h)`
     */
    monitor?: string;
    /**
     * Update order either 'stop-first' or 'start-first'.
     */
    order?: string;
    /**
     * The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).
     */
    parallelism?: number;
}

export interface VolumeLabel {
    label: string;
    value: string;
}
export namespace config {
    export interface RegistryAuth {
        address: string;
        configFile?: string;
        configFileContent?: string;
        password?: string;
        username?: string;
    }
}

