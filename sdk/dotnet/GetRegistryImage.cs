// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi.Utilities;

namespace Pulumi.Docker
{
    public static class GetRegistryImage
    {
        /// <summary>
        /// Reads the image metadata from a Docker Registry. Used in conjunction with the docker.RemoteImage resource to keep an image up to date on the latest available version of the tag.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Docker = Pulumi.Docker;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var ubuntuRegistryImage = Output.Create(Docker.GetRegistryImage.InvokeAsync(new Docker.GetRegistryImageArgs
        ///         {
        ///             Name = "ubuntu:precise",
        ///         }));
        ///         var ubuntuRemoteImage = new Docker.RemoteImage("ubuntuRemoteImage", new Docker.RemoteImageArgs
        ///         {
        ///             Name = ubuntuRegistryImage.Apply(ubuntuRegistryImage =&gt; ubuntuRegistryImage.Name),
        ///             PullTriggers = 
        ///             {
        ///                 ubuntuRegistryImage.Apply(ubuntuRegistryImage =&gt; ubuntuRegistryImage.Sha256Digest),
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetRegistryImageResult> InvokeAsync(GetRegistryImageArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRegistryImageResult>("docker:index/getRegistryImage:getRegistryImage", args ?? new GetRegistryImageArgs(), options.WithVersion());

        /// <summary>
        /// Reads the image metadata from a Docker Registry. Used in conjunction with the docker.RemoteImage resource to keep an image up to date on the latest available version of the tag.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Docker = Pulumi.Docker;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var ubuntuRegistryImage = Output.Create(Docker.GetRegistryImage.InvokeAsync(new Docker.GetRegistryImageArgs
        ///         {
        ///             Name = "ubuntu:precise",
        ///         }));
        ///         var ubuntuRemoteImage = new Docker.RemoteImage("ubuntuRemoteImage", new Docker.RemoteImageArgs
        ///         {
        ///             Name = ubuntuRegistryImage.Apply(ubuntuRegistryImage =&gt; ubuntuRegistryImage.Name),
        ///             PullTriggers = 
        ///             {
        ///                 ubuntuRegistryImage.Apply(ubuntuRegistryImage =&gt; ubuntuRegistryImage.Sha256Digest),
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetRegistryImageResult> Invoke(GetRegistryImageInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRegistryImageResult>("docker:index/getRegistryImage:getRegistryImage", args ?? new GetRegistryImageInvokeArgs(), options.WithVersion());
    }


    public sealed class GetRegistryImageArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        /// </summary>
        [Input("insecureSkipVerify")]
        public bool? InsecureSkipVerify { get; set; }

        /// <summary>
        /// The name of the Docker image, including any tags. e.g. `alpine:latest`
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetRegistryImageArgs()
        {
        }
    }

    public sealed class GetRegistryImageInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        /// </summary>
        [Input("insecureSkipVerify")]
        public Input<bool>? InsecureSkipVerify { get; set; }

        /// <summary>
        /// The name of the Docker image, including any tags. e.g. `alpine:latest`
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetRegistryImageInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetRegistryImageResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        /// </summary>
        public readonly bool? InsecureSkipVerify;
        /// <summary>
        /// The name of the Docker image, including any tags. e.g. `alpine:latest`
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The content digest of the image, as stored in the registry.
        /// </summary>
        public readonly string Sha256Digest;

        [OutputConstructor]
        private GetRegistryImageResult(
            string id,

            bool? insecureSkipVerify,

            string name,

            string sha256Digest)
        {
            Id = id;
            InsecureSkipVerify = insecureSkipVerify;
            Name = name;
            Sha256Digest = sha256Digest;
        }
    }
}
