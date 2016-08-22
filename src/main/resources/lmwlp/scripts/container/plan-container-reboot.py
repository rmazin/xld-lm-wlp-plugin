#
from java.util import HashMap
from java.util import HashSet
from com.xebialabs.deployit.plugin.api.deployment.planning import DefaultOrders


def containers():
    result = HashSet()
    for delta in deltas.deltas:
        deployed = delta.deployedOrPrevious
        current_container = deployed.container
        if delta.operation != "NOOP" and current_container.type == "wlp.Server" and current_container.rebootServer is True:
            result.add(current_container)
    return result


for container in containers():
    fc = {'container':container}
    context.addStep(steps.os_script(
       description="rebooting container: %s on %s" % (container.name, container.host.name) ,
       script="lmwlp/scripts/container/server-restart-container",
       freemarker_context=fc,
       order=99,
       target_host = container.host))

