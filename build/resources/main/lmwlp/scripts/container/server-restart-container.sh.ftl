sudo /util/mware/was/startStopLP.sh -a stop -s ${container.name}
rc=$?

case $rc in
	0) echo "Server ${container.name} stopped"
	;;
	1) echo "Server ${container.name} is already stopped"
	;;
	2) echo "Server ${container.name} does not exist" >&2
	exit $rc
	;;
	*) echo "An error occurred while stopping server ${container.name}" >&2
	exit $rc
	;;
esac



sudo /util/mware/was/startStopLP.sh -a start -s ${container.name} -clean
rc=$?

case $rc in
	0) echo "Server ${container.name} started"
	exit 0
	;;
	1) echo "Server ${container.name} is already running"
	exit 0
	;;
	2) echo "Server ${container.name} does not exist" >&2
	exit $rc
	;;
	*) echo "An error occurred while starting server ${container.name}" >&2
	exit $rc
	;;
esac


