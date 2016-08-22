# this script is responsible for adding steps to the undeployment plan in case of the undeployment of an xml file

from wlp.modules.utility import Paths
from com.xebialabs.deployit.plugin.api.deployment.specification import Operation
from com.xebialabs.deployit.plugin.api.deployment.planning import DefaultOrders

previousDeployed.location = "%s/%s" % (Paths.get_server_config_dir(previousDeployed.container),  previousDeployed.name)

context.addStepWithCheckpoint(steps.jython(
    description="Remove configuration entry: %s from: %s" % (previousDeployed.name, previousDeployed.container.name),
    script="wlp/scripts/resource/destroy-resource.py",
    order=DefaultOrders.UNDEPLOY_ARTIFACTS
), delta, Operation.DESTROY)

context.addStepWithCheckpoint(steps.delete(
    description="removing imported xml file: %s from %s" % (previousDeployed.name, previousDeployed.container.name),
    target_path=previousDeployed.location,
    order=DefaultOrders.UNDEPLOY_ARTIFACTS + 1
), delta, Operation.DESTROY)
