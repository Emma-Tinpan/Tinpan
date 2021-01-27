# GitLabをDockerコンテナで起動する方法

## 以下のコマンドでGitLabのコンテナが起動ができる
```bash
$ docker run --detach \
    --hostname gitlab.example.com \
    --publish 443:443 --publish 80:80 \
    --name gitlab \
    --restart always \
    --volume $GITLAB_HOME/config:/etc/gitlab \
    --volume $GITLAB_HOME/logs:/var/log/gitlab \
    --volume $GITLAB_HOME/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest
```
<br>
<br>

### 補足  
$GITLAB_HOMEの設定方法
```bash
//PATHを通す
$ export GITLAB_HOME=$PWD/gitlab
//設定変更を反映
source ~/.bash_profile
```
<br>
<br>
<br>
コンテナ起動後  

docker exec -it gitlab gitlab-ctl reconfigure