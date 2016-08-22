# this script is responsible for adding steps to the deployment plan in case of the deployment of an xml file

from wlp.modules.utility import Paths
from com.xebialabs.deployit.plugin.api.deployment.specification import Operation
from com.xebialabs.deployit.plugin.api.deployment.planning import DefaultOrders




deployed.location = "%s/%s" % (Paths.get_server_config_dir(deployed.container),  deployed.name)

context.addStepWithCheckpoint(steps.upload(
    description="Upload xml '%s' to server '%s'" % (deployed.name, deployed.container.name),
    target_path=deployed.location,
    order=DefaultOrders.DEPLOY_ARTIFACTS + deployed.rank
), delta, Operation.CREATE)


