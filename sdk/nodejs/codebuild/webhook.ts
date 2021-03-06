// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a CodeBuild webhook, which is an endpoint accepted by the CodeBuild service to trigger builds from source code repositories. Depending on the source type of the CodeBuild project, the CodeBuild service may also automatically create and delete the actual repository webhook as well.
 * 
 * ## Example Usage
 * 
 * ### Bitbucket and GitHub
 * 
 * When working with [Bitbucket](https://bitbucket.org) and [GitHub](https://github.com) source CodeBuild webhooks, the CodeBuild service will automatically create (on `aws_codebuild_webhook` resource creation) and delete (on `aws_codebuild_webhook` resource deletion) the Bitbucket/GitHub repository webhook using its granted OAuth permissions. This behavior cannot be controlled by Terraform.
 * 
 * > **Note:** The AWS account that Terraform uses to create this resource *must* have authorized CodeBuild to access Bitbucket/GitHub's OAuth API in each applicable region. This is a manual step that must be done *before* creating webhooks with this resource. If OAuth is not configured, AWS will return an error similar to `ResourceNotFoundException: Could not find access token for server type github`. More information can be found in the CodeBuild User Guide for [Bitbucket](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-bitbucket-pull-request.html) and [GitHub](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-github-pull-request.html).
 * 
 * > **Note:** Further managing the automatically created Bitbucket/GitHub webhook with the `bitbucket_hook`/`github_repository_webhook` resource is only possible with importing that resource after creation of the `aws_codebuild_webhook` resource. The CodeBuild API does not ever provide the `secret` attribute for the `aws_codebuild_webhook` resource in this scenario.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.codebuild.Webhook("example", {
 *     projectName: aws_codebuild_project_example.name,
 * });
 * ```
 */
export class Webhook extends pulumi.CustomResource {
    /**
     * Get an existing Webhook resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WebhookState, opts?: pulumi.CustomResourceOptions): Webhook {
        return new Webhook(name, <any>state, { ...opts, id: id });
    }

    /**
     * A regular expression used to determine which branches get built. Default is all branches are built.
     */
    public readonly branchFilter!: pulumi.Output<string | undefined>;
    /**
     * The CodeBuild endpoint where webhook events are sent.
     */
    public /*out*/ readonly payloadUrl!: pulumi.Output<string>;
    /**
     * The name of the build project.
     */
    public readonly projectName!: pulumi.Output<string>;
    /**
     * The secret token of the associated repository. Not returned by the CodeBuild API for all source types.
     */
    public /*out*/ readonly secret!: pulumi.Output<string>;
    /**
     * The URL to the webhook.
     */
    public /*out*/ readonly url!: pulumi.Output<string>;

    /**
     * Create a Webhook resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WebhookArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WebhookArgs | WebhookState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as WebhookState | undefined;
            inputs["branchFilter"] = state ? state.branchFilter : undefined;
            inputs["payloadUrl"] = state ? state.payloadUrl : undefined;
            inputs["projectName"] = state ? state.projectName : undefined;
            inputs["secret"] = state ? state.secret : undefined;
            inputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as WebhookArgs | undefined;
            if (!args || args.projectName === undefined) {
                throw new Error("Missing required property 'projectName'");
            }
            inputs["branchFilter"] = args ? args.branchFilter : undefined;
            inputs["projectName"] = args ? args.projectName : undefined;
            inputs["payloadUrl"] = undefined /*out*/;
            inputs["secret"] = undefined /*out*/;
            inputs["url"] = undefined /*out*/;
        }
        super("aws:codebuild/webhook:Webhook", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Webhook resources.
 */
export interface WebhookState {
    /**
     * A regular expression used to determine which branches get built. Default is all branches are built.
     */
    readonly branchFilter?: pulumi.Input<string>;
    /**
     * The CodeBuild endpoint where webhook events are sent.
     */
    readonly payloadUrl?: pulumi.Input<string>;
    /**
     * The name of the build project.
     */
    readonly projectName?: pulumi.Input<string>;
    /**
     * The secret token of the associated repository. Not returned by the CodeBuild API for all source types.
     */
    readonly secret?: pulumi.Input<string>;
    /**
     * The URL to the webhook.
     */
    readonly url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Webhook resource.
 */
export interface WebhookArgs {
    /**
     * A regular expression used to determine which branches get built. Default is all branches are built.
     */
    readonly branchFilter?: pulumi.Input<string>;
    /**
     * The name of the build project.
     */
    readonly projectName: pulumi.Input<string>;
}
