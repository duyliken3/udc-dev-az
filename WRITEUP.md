# Write-up Template

## Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Decissions and Comparisons

#### Cost

- The App Service will have lower cost than VM which consume resources, like CPU and memory, even though when the application is not in use.

#### Availability

- Both of VM and App Service have high availability.

### Scalability

- Azure App Service has constraints in terms of scalability. Azure VMs are preferred for apps, which have the scope to expand for the future.

#### Solution/Choice for current CMS App

The best option for this CMS App is App Service. It offers less flexibility and less control than VM but I dont need full control of the infrastructure. My goal is just to run a simple python flask webapp.

### Assess app changes that would change your decision.

Disadvantages of App Service as opposed to VM

- Hardware limitations: maximum of 14GB RAM and 4 vCPU cores per instance
- Limited set of supported languages
- Payment for active Service Plan even if application is not running

Should the requirements change in future then the App Service disadvantages listed above would have to be taken in account. E.g. if the web app was to change to an unsupported language then VM would offer the flexibility to install any SW required to run it. Or if the app computational demands grow above the max limit for App Service then a VM with much larger computational capacity could be easily selected.