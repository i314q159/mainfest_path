# mainfest_path

+ find_git.sh > 8mp_android11_path.txt，获得形如./packages/modules/IPsec/.git这样格式的路径
+ main.py生成xml里面的project节点的xml文件
+ 拼接完整的xml文件，加入remote和default节点，fetch是相对于于gerrit存放裸仓库的位置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
    <remote name="origin"
        fetch="asu_android_11/"
        review="ssh://192.168.10.100:29418/" />
    <default revision="master"
        remote="origin"
        sync-j="4" />
</manifest>
```
