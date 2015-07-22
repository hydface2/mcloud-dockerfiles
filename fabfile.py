from fabric.operations import local


def build():
    for plugin in (
        'mcloud',
        'mcloud-osx',
    ):
        local('docker build -t mcloud/%(plugin)s %(plugin)s' % {'plugin': plugin})
