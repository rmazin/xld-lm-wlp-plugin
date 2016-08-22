# this script is responsible for adding steps to the undeployment plan in case of the undeployment of an xml file

from wlp.modules.utility import Paths
from com.xebialabs.deployit.plugin.api.deployment.specification import Operation
from com.xebialabs.deployit.plugin.api.deployment.planning import DefaultOrders

location = "%s/%s" % (Paths.get_server_config_dir(previousDeployed.container),  previousDeployed.name)

context.addStepWithCheckpoint(steps.delete(
    description="removing config file: %s from %s" % (previousDeployed.name, previousDeployed.container.name),
    target_path=location
), delta, Operation.DESTROY)
