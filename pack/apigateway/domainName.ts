// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class DomainName extends lumi.NamedResource implements DomainNameArgs {
    public readonly certificateArn?: string;
    public readonly certificateBody?: string;
    public readonly certificateChain?: string;
    public readonly certificateName?: string;
    public readonly certificatePrivateKey?: string;
    public /*out*/ readonly certificateUploadDate: string;
    public /*out*/ readonly cloudfrontDomainName: string;
    public /*out*/ readonly cloudfrontZoneId: string;
    public readonly domainName: string;

    constructor(name: string, args: DomainNameArgs) {
        super(name);
        this.certificateArn = args.certificateArn;
        this.certificateBody = args.certificateBody;
        this.certificateChain = args.certificateChain;
        this.certificateName = args.certificateName;
        this.certificatePrivateKey = args.certificatePrivateKey;
        if (lumirt.defaultIfComputed(args.domainName, "") === undefined) {
            throw new Error("Property argument 'domainName' is required, but was missing");
        }
        this.domainName = args.domainName;
    }
}

export interface DomainNameArgs {
    readonly certificateArn?: string;
    readonly certificateBody?: string;
    readonly certificateChain?: string;
    readonly certificateName?: string;
    readonly certificatePrivateKey?: string;
    readonly domainName: string;
}
