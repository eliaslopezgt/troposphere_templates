#tool "nuget:?package=GitVersion.CommandLine"
#addin "nuget:?package=Cake.DotNetCoreEf"
#addin "nuget:?package=Cake.Terraform"

var target = Argument("target", "Default");

Task("Default")
    .Does(() =>
    {
        Information("Hello World!");
    });
RunTarget(target);