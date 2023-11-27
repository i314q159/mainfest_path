# gerrit_path

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
    <remote name="origin"
        fetch="asu_android_11/"
        review="ssh://192.168.10.100:29418/" />
    <default revision="master"
        remote="origin"
        sync-j="4" />
    <project name="a" path="a" />

</manifest>
```