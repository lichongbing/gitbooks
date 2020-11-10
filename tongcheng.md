# 资源地址

阿里云，2核心4G  5M带宽    系统ubuntu18.04版本系统安装宝塔面板，服务器环境，nginx1.6+php7.1+mysql5.6

商城的网址[https://tongcheng.yuelingnet.cn](https://tongcheng.yuelingnet.cn)

商城后台网址:[https://tongcheng.yuelingnet.cn/admin/](https://tongcheng.yuelingnet.cn/admin/)

 im网站[https://sns.yuelingnet.cn/im/h5/](https://sns.yuelingnet.cn/im/h5/)

 im源码地址[https://Lichongbing@bitbucket.org/Lichongbing/im.makerjie.com.git](https://Lichongbing@bitbucket.org/Lichongbing/im.makerjie.com.git)
 

 
 
# im安装部署说明


环境apache2.4+mysql5.6数据库


1：如果报错： 宝塔修改user.ini文件  open_basedir里面的删除一级目录/cpccc-web/

2：/cpccc-web/config/  配置数据库信息


3:运行目录：/cpccc-web/public  不要开启防跨站攻击【修改user.ini】

  【示范案例】open_basedir=/www/wwwroot/你网站的目录/:/tmp/:/proc/

   

4：开启https  不要强制开启，配置一定要注意


linux命令

5：检测环境：
```
curl -Ss http://www.workerman.net/check.php | php  #如果有禁用函数要取消
```
6：下载命令：
```
git clone https://github.com/walkor/Workerman
``` 

安装步骤

7：修改数据库：setting  字段：ws_address 的域名值

8：宝塔》》站点管理》》配置文件》》》

找到代码：SSLProxyEngine on  下面加上阿里云安全组跟宝塔后台安全组要加6060  443  端口
```

ProxyRequests Off
ProxyPass /app ws://127.0.0.1:6060/app
ProxyPassReverse /app ws://127.0.0.1:6060/app
open_basedir=/www/wwwroot/im.jintaocms.com/:/tmp/:/proc/
```
9：cd到目录启动

```
CD1： cd /www/wwwroot/im.jintaocms.com/cpccc-socket【CD到你自己的目录】
CD2： cd /www/wwwroot/im.tqzfwl.cn/cpccc-socket
CD3： cd /www/wwwroot/im.niukea.com/cpccc-socket
CD4： cd /www/wwwroot/im.shenghuozx.cn/cpccc-socket

CD5： cd /www/wwwroot/im.xincor.cn/cpccc-socket

```
以debug（调试，关闭ssh后不生效了，调试用这个）方式启动
```
php start.php start
```
以daemon（守护进程，运营后用这个方法）方式启动
```
php start.php start -d
```
停止
```
php start.php stop
```
重启
```
php start.php restart
```
平滑重启
```
php start.php reload
```
查看状态
```
php start.php status
```
查看连接状态（需要Workerman版本>=3.5.0）
```
php start.php connections
```


lsof -i【查看全部端口】
```
lsof -i:4568
```

看云手册：[http://doc3.workerman.net/315117](http://doc3.workerman.net/315117)


错误解决：

端口2020  6060  等端口都要打开


宝塔外网面板地址: [http://47.99.221.64:8888/c6dbcb2b](http://47.99.221.64:8888/c6dbcb2b)

username: xxszqae6

password: f1f06c14

shell终端登录：47.99.221.64 
username:root
password:xgkLIJIN@369

# 聊天对接文档说明：


## 整合api

1：url模式访问即可换起聊天功能【已可生成二维码】php用phpqrcode生成连接

u：发起人会员用户ID【唯一值】

n：发起人用户手机

a：发起人自己头像

s：发起人自己的地址

tu：对方的ID【被聊天对象】【唯一值】

tn：对方的名字【被聊天对象】

ta：对方的头像【被聊天对象】

ts：地址比如重庆【被聊天对象】

url：回调url，返回对接的网站【被聊天对象】

demo

[https://im.baidu.com/uis.php?u=30986&n=17194348115&a=&s=&tu=30851&tn=陈禹同&ta=https://wyinchengcastingidu.com/data/upload/user/20191014/make15761705383.JPG&ts=重庆市&url=https://baidu.com/wap/resume.html](https://im.baidu.com/uis.php?u=30986&n=17194348115&a=&s=&tu=30851&tn=陈禹同&ta=https://wyinchengcastingidu.com/data/upload/user/20191014/make15761705383.JPG&ts=重庆市&url=https://baidu.com/wap/resume.html)


## 整合余额红包
您网站会员ID跟IM会员ID一致

1：IM数据库跟网站数据库安装一个数据库下面

2：您的网站修改余额时候修改IM下面相同ID的余额

3：您IM网站修改余额的时候修改下您网站的会员ID的余额

## C整合Baocms的API下面是会员跟商家对话
>html文件：themes\default\wap\shop\detail.html

```php
<php>

$u= M('users')->where(array('user_id'=>$MEMBER['user_id']))->find();
$to= M('users')->where(array('user_id'=>$detail['user_id']))->find();
$furl = $CONFIG['site']['host']."/wap/shop/detail/shop_id/".$detail['shop_id'];

$url = "https://im.niukea.com/uis.php?u=".$u['user_id']."&n=".$u['nickname']."&a=".config_weixin_img($u['face'])."&s=&tu=".$to['user_id']."&tn=".$to['nickname']."&ta=".config_weixin_img($to['face'])."&ts=重庆市&url=".$furl;

$false = 0;
if($MEMBER['user_id'] == $detail['user_id'] || empty($MEMBER['user_id']) || empty($detail['user_id'])){
 $false = 0;
}else{
 $false = 1;
}

</php>


<if condition="$false"> 
    <div class="blank-10 bg"></div>
    <div class="container2" style="margin:10px;">
        <div class="form-button"><a href="<{$url}>" class="button button-block button-big bg-dot text-center" type="submit">联系商家客服</a></div>
    </div>
</if> 

```

## 整合jintaocms的tp5
php文件：application/wap/controller/shop.php


```php
//整合IM开始加方法detail里面


  $config = Setting::config();
  $imhost = $config['site']['imhost'];
  
  $u= Db::name('users')->where(array('user_id'=>$this->uid))->find();
  $to= Db::name('users')->where(array('user_id'=>$detail['user_id']))->find();
  
  $furl = $config['site']['host']."/wap/shop/detail/shop_id/".$detail['shop_id'];
  $url = $imhost."/uis.php?u=".$u['user_id']."&n=".$u['nickname']."&a=".config_weixin_img($u['face'])."&s=&tu=".$to['user_id']."&tn=".$to['nickname']."&ta=".config_weixin_img($to['face'])."&ts=重庆市&url=".$furl;
  
  $im = 0;
  if($this->uid == $detail['user_id'] || empty($this->uid) || empty($detail['user_id']) || empty($imhost)){
   $im = 0;
  }else{
   $im = 1;
  }
  $this->assign('im',$im);
  $this->assign('url',$url);
```

>html文件：application\wap\view\shop\detail.html
```html
 {if condition="$im"}
        <div class="blank-10 bg"></div>
        <div class="container2" style="margin:10px;">
            <div class="form-button"><a href="{$url}" class="button button-block button-big bg-dot text-center" type="submit">联系商家客服</a></div>
        </div>
    {/if} 

```   


