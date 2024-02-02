# Description

`template.yml` is the SAM template that gets updated from the `cfn-deploy.yml` template.

The `cfn-deploy.yml` template has a build phase that packages the `template.yml` from the github source.

Then, it gets to a deploy phase, which will cause a stack UPDATE to the already deployed `template.yml` file. If the template isn't already deployed, it will create a new stack.
