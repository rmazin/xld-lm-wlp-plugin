#
from java.util import HashMap
from java.util import HashSet
from com.xebialabs.deployit.plugin.api.deployment.planning import DefaultOrders

logger.info("starting planning phase for update features")

def containers():
    result = HashSet()
    for delta in deltas.deltas:
        deployed = delta.deployedOrPrevious
        current_container = deployed.container
        if current_container.type == "wlp.Server":
            logger.info("adding container: %s to the containers to update their features" % current_container )
            result.add(current_container)
    return result

def update_needed():
    for delta in deltas.deltas:
        deployed = delta.deployedOrPrevious
        if delta.operation != "NOOP" and delta.operation != "DESTROY" and deployed.type == "lmwlp.IncludedXml":
            logger.info("artifact: %s warrents an update of features" % deployed.name )
            return True
    return False


if update_needed() is True:

    for container in containers():
        logger.info("update of features needed on %s" % container.name)
        fc = {'container':container}
        context.addStep(steps.os_script(
          description="Installing new features for: %s on %s" % (container.name, container.host.name) ,
          script="lmwlp/scripts/configuration/install-features",
          freemarker_context=fc,
          order=99,
          target_host = container.host))

logger.info("done with planning phase for update features")
