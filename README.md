The goal of this project is to provide set of utilities to assess network configuration of a VNET injected workspace, according to Databricks mandatory and recommanded rules

## Azure Databricks : What is vnet-injected Workspace ?

The default deployment of Azure Databricks is a fully managed service on Azure: all data plane resources, including a virtual network (VNet) that all clusters will be associated with, are deployed to a locked resource group. 

If you require network customization, however, you can deploy Azure Databricks data plane resources in your own virtual network (sometimes called [VNet injection](https://docs.azuredatabricks.net/administration-guide/cloud-configurations/azure/vnet-inject.html)), enabling you to:

- Connect Azure Databricks to other Azure services (such as Azure Storage) in a more secure manner using [service endpoints](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview).
- Connect to on-premises data sources for use with Azure Databricks, taking advantage of [user-defined routes](https://docs.azuredatabricks.net/administration-guide/cloud-configurations/azure/udr.html#udr).
- Connect Azure Databricks to a [network virtual appliance](https://docs.azuredatabricks.net/administration-guide/cloud-configurations/azure/on-prem-network.html#route-via-firewall) to inspect all outbound traffic and take actions according to allow and deny rules.
- Configure Azure Databricks to use custom [DNS](https://docs.azuredatabricks.net/administration-guide/cloud-configurations/azure/on-prem-network.html#vnet-custom-dns).
- Configure network security group ([NSG](https://docs.microsoft.com/en-us/azure/virtual-network/manage-network-security-group)) rules to specify egress traffic restrictions.
- Deploy Azure Databricks clusters in your existing virtual network.


## Vnet-injection Sanity Checks

- Validity of NSG and inbound/outbound rules : verify that [traffic subnet whitelistening](https://docs.azuredatabricks.net/administration-guide/cloud-configurations/azure/vnet-inject.html#whitelisting-subnet-traffic) is correctly implemented  
- Validity of VNET and subnets : The virtual network must include two subnets dedicated to Azure Databricks
   * A private subnet with a configured [network security group](https://docs.microsoft.com/en-us/azure/virtual-network/manage-network-security-group) that allows cluster-internal communication.
   * A public subnet with a configured network security group that allows communication with the Azure Databricks control plane
- Validity of any peering done on the existing VNET, and see if it has a firewall or a ER gateway
- Validity of any route table attached to the subnets : verify that all rules comply with Databricks Inbound/Outbound rules
- Validity of any custom DNS set on the VNET

