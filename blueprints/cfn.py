from troposphere import (
    Base64, GetAtt, FindInMap, Join, Output, Ref, Parameter, Template
)
from troposphere.s3 import (
    Bucket, PublicRead, WebsiteConfiguration
)
from troposphere.cloudfront import (
    Distribution, DistributionConfig, Origin, CustomOrigin, CacheBehavior, DefaultCacheBehavior, Cookies, ForwardedValues, S3Origin, Logging
)
from stacker.blueprints.base import Blueprint

class CFN(Blueprint):
    def create_s3_bucket(self):
        self.s3Bucket = self.add_resource(Bucket(
            "S3Bucket",
            AccessControl=PublicRead,
            WebsiteConfiguration=WebsiteConfiguration(
                IndexDocument="index.html",
                ErrorDocument="error.html"
                )
            ))
        self.add_output([
            Output(
                "WebsiteURL",
                Value=GetAtt(self.s3Bucket, "WebsiteURL"),
                Description="URL for website hosted on S3"
                ),
            Output(
                "S3BucketSecureURL",
                Value=Join("", ["http://", GetAtt(self.s3Bucket, "DomainName")]),
                Description="Name of S3 bucket to hold website content"
                ),
            ])

    def create_template(self):
        self.create_s3_bucket();
