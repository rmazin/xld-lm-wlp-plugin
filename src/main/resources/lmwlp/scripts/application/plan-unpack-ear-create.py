# this script will add three steps to a plan for each module being deployed to targetPath
# step 1: unpack ear : this will unpack a already deployed earfile in place in the apps directory of webshpere liberty profile
# step 2: unpack war : this will unpack all war files found inside the unpacked earfile
# step 4: update application.xml. this will augment the appliction.xml with the new paths inside the ear after war unpack
#
#These steps will be added for each

from wlp.modules.utility import Paths
from com.xebialabs.deployit.plugin.api.deployment.specification import Operation
from com.xebialabs.deployit.plugin.api.deployment.planning import DefaultOrders



if deployed.unpackZipFile is True:
    fc = {'deployed': deployed,
          'targetPath': "%s/apps" % (Paths.get_server_config_dir(deployed.container))}
    context.addStepWithCheckpoint(steps.os_script(
        description="unpacking earfile: %s " % (deployed.name) ,
        script="lmwlp/scripts/application/unpack-ear",
        freemarker_context=fc,
        order=DefaultOrders.DEPLOY_ARTIFACTS + 4,
        target_host = deployed.container.host
    ), delta, Operation.CREATE)
    context.addStepWithCheckpoint(steps.os_script(
        description="unpacking warfiles for application: %s " % (deployed.name) ,
        script="lmwlp/scripts/application/unpack-war",
        freemarker_context=fc,
        order=DefaultOrders.DEPLOY_ARTIFACTS + 5,
        target_host = deployed.container.host
    ), delta, Operation.CREATE)
    context.addStepWithCheckpoint(steps.os_script(
        description="update application xml for application: %s " % (deployed.name) ,
        script="lmwlp/scripts/application/update-application-xml",
        freemarker_context=fc,
        order=DefaultOrders.DEPLOY_ARTIFACTS + 6,
        target_host = deployed.container.host
    ), delta, Operation.CREATE)
    context.addStepWithCheckpoint(steps.os_script(
        description="add .ear to the expanded directory: %s " % (deployed.name) ,
        script="lmwlp/scripts/application/update-application-path",
        freemarker_context=fc,
        order=DefaultOrders.DEPLOY_ARTIFACTS + 7,
        target_host = deployed.container.host
    ), delta, Operation.CREATE)
