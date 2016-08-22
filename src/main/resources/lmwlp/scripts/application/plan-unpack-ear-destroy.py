#This script adds steps to an undeploy plan to get the ear back into a zipped format
# it only uses one script wich goes into the apps directory and zip up the formerly expanded directory so that xld can then handle the undeploy

from wlp.modules.utility import Paths
from com.xebialabs.deployit.plugin.api.deployment.specification import Operation
from com.xebialabs.deployit.plugin.api.deployment.planning import DefaultOrders


if previousDeployed.unpackZipFile is True:

    fc = {'previousDeployed': previousDeployed,
          'targetPath': "%s/apps" % (Paths.get_server_config_dir(previousDeployed.container))}

    context.addStepWithCheckpoint(steps.os_script(
        description="repacking earfile: %s " % (previousDeployed.name) ,
        script="lmwlp/scripts/application/pack-ear",
        freemarker_context=fc,
        order=DefaultOrders.UNDEPLOY_ARTIFACTS - 1 ,
        target_host = previousDeployed.container.host
    ), delta, Operation.DESTROY)
