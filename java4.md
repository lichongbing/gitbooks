<a id="1"></a>
## 整理实战JavaWeb项目

<a id="2"></a>
### 微人事项目实战

#### 要点

* 微人事项目介绍

* 项目技术架构

* 前后端分离项目构建

* 登录模块实现

* 动态加载用户菜单

* 邮件发送

* 员工资料导入导出

* 在线聊天

* 前端项目打包

本章将通过一个前后端分离项目带读者掌握目前流行的Spring Boot+Vue前后端分离开发环境
的搭建以及项目的开发流程。本章重点向读者介绍前后端分离环境的搭建以及开发流程，也涉及少
量的业务逻辑。
本章项目的完整代码可以在GitHub上下载，下载地址为[https://github.com/lenve/vi](https://github.com/lenve/vi),本章在展示代码时仅展示项目关键步骤的核心代码。



### 项目简介

人事管理系统是一种常见的企业后台管理系统，它的主要目的是加强各个部门之间的协调提高工作效率。人事管理系统提供了员工资料管理、人事管理、工资管理、统计管理以及系统管理等功能，通过人事管理统，人事组织部门能做到以人为中心，各部门之间实现资源共享，并且实现即时通信，提高工作效率，简化烦琐的手工统计、信息汇总和工资业务等大量的人工工作，让人事组织和工资管理工作在人事组织相关的部门之间活跃起来。


### 技术架构
本项目采用当下流行的前后端分离的方式开发，后端使用 Spring Boot开发，前端使用Vue+ElementUI来构建SPA.SPA 是指 Single-Page Application,即单页面应用，SPA应用通过动 本重写当前页面来与用户交互，而非传统的从服务器重新加载整个新页面。这种方法避免了页面之间切换打断用户体验，使应用程序更像一个桌面应用程序。在SPA中，所有的HTML、JavaScript和CSS都通过单个页面的加载来检索，或者根据用户操作动态装载适当的资源并添加到页面。在SPA中，前端将通过Ajax与后端通信。对于开发者而言，SPA最直观的感受就是项目开发完成后，只有一个 HTML页面，所有页面的跳转都通过路由进行导航。前后端分离的另一个好处是一个后端可以对应多个前端，由于后端只负责提供数据，前后端的交互都是通过JSON数据完成的，因此后端开发成功后，前端可以是PC端页面，也可以是Android、iOS以及微信小程序等。


#### Vue简介


Vue(读音／vju:/,类似于 view)是一套用于构建用户界面的渐进式框架。与其他大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 完全能够为复杂的单页应用提供驱动。－Vue 官网


对于Vue的基础知识，本书不做过多介绍，由于Vue的文档都是中文文档，因此强烈建议初字者通读官方文档来了解Vue 的基本使用方法（地址为 https://cn.vuejs.org/v2/guide/),本书后面将直接介绍Vue 在项目中的使用。

#### Element 简介
Vue 桌面端组件库非常多，比较流行的有 Element、Vux、iView、mint-ui、muse-ui等，本项术用 Element 作为前端页面组件库。要说设计，这些UI库差异都不是很大，基本上都是Materialcsign 风格的，本项目采用 Element 主要考虑到该库的使用人数较多（截至写作本书时，Element的GitHub上的 star数已达 29000,接近30000),出了问题容易找到解决方案。关于Element的，强烈建议初学者通读官方文档学习（地址为http://element-cn.eleme.io/#/zh-CN/component). 


#### 其他

除了前端技术点外，后端用到的技术主要就是第1~15 章提到的技术，这里就不详细展开了
章
### 项目构建

#### 前端项目构建


Vue 项目使用 webpack 来构建。首先确保本地已经安装了 NodeJS,然后在CMD中执行如下
令，可以创建并启动一个名为vuehr的前端项目：

```
npm install -g vue-cli
vue init webpack vuehr
cd vuehr
npm run dev
```
在执行“vue init webpack vuehr”命令时，会要求依次输入项目的基本信息，如图16-1所示。

```
Project name vuehr
Project description A Vue.js project
Author 江南一点雨
＜wangsong0210@gmail.com
Vue build standalone
Install vue-router?ies
Use ESLint to lint your code?No
Set up unit tests No
Setup e2e tests with Nightwatch?No
Should we run npm install for you after the project has been created?(recommended)nom 
vue-cli
Generated vuehr".
```


### 基本信息主要包括：

* 项目名称。

* 项目描述。

* 项目作者。

* Vue 项目构建：运行＋编译还是仅运行。

* 是否安装 vue-router.

* 是否使用 ESLint.

* 是否使用单元测试。

* 是否适用 Nightwatch e2e 测试。

* 是否在项目创建成功后自动执行“npm install”安装依赖，若选择否，则在第4行命令执行之
前执行“npm install”。

当“npm run dev”命令执行之后，在浏览器中输入 http://localhost:8080,显示页面
### 后端项目构建

后端使用 Spring Boot 创建一个 Spring Boot工程，添加 spring-boot-starter-web 依赖即可：

```xml
＜dependency> 
＜groupId>org.springframework.boot</groupId>
＜artifactId>spring-boot-starter-web</artifactId>
＜／dependency>
```
当然，后端所需的依赖不止spring-boot-starter-web,在后文功能不断完善的过程中，再继续鼎具他依赖。另外，后端项目所需的Redis 配置、邮件发送配置、POI配置、WebSocket配置等将在涉及相关功能时向读者介绍。

### 数据模型设计


完整的数据库脚本可以在 GitHub 上下载，下载地址为[https://github.com/lenve/vhr/blob/master/hrserver/src/main/resources/vhr.sql](https://github.com/lenve/vhr/blob/master/hrserver/src/main/resources/vhr.sql),这里仅展示本项目的数据字典。


adjustsalary表（员工调薪表）

| 字段名  |逻辑名   | 数据类型  | 约束  | 说明  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| id  |   | Integer  | 主键，自增长  | 主键  |
|  eid |   |  Integer |外键，普通索引   | 员工id  |
|  asDate |   | Date  |   | 调薪日期  |
|  beforeSalary |   |  Integer |   |  调前薪资 |
| afterSalary  |   |  Integer |   |调后薪资   |
|  reason |   | String(255)  |   | 调薪原因  |
| remark  |   |  String(255) |   | 备注  |

appraise表（员工评价表）


| 字段名  |逻辑名   | 数据类型  | 约束  | 说明  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| id  |   | Integer  | 主键，自增长  | 主键  |
|  eid |   |  Integer |外键，普通索引   | 员工id  |
|  appDate |   | Date  |   | 考评日期  |
|  appResult |   |  String(255) |   |  考评结果 |
|  appContent |   |  String(255) |   |  考评内容 |
| remark  |   |  String(255) |   | 备注  |


department表（部门表）


| 字段名  |逻辑名   | 数据类型  | 约束  | 说明  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| id  |   | Integer  | 主键，自增长  | 主键  |
|  name |   |  String(32) |  | 部门名称  |
|  parentId |   | Date  |   | 父部门id |
|  depPath |   |  String(255) |   |  部门path |
|  enabled |   |  Enum |   |  是否可用 |
| isParent  |   |  Enum  |   | 是否为父部门  |


employee表（员工信息表）


| 列名           | 数据类型                                                     | 字段类型 | 长度 | 是否为空 | 默认值 | 备注         |
| -------------- | ------------------------------------------------------------ | -------- | ---- | -------- | ------ | ------------ |
| address        | varchar(64)                                                  | varchar  | 64   | YES      |        | 联系地址     |
| beginContract  | date                                                         | date     |      | YES      |        | 合同起始日期 |
| beginDate      | date                                                         | date     |      | YES      |        | 入职日期     |
| birthday       | date                                                         | date     |      | YES      |        | 出生日期     |
| contractTerm   | double                                                       | double   |      | YES      |        | 合同期限     |
| conversionTime | date                                                         | date     |      | YES      |        | 转正日期     |
| departmentId   | int(11)                                                      | int      |      | YES      |        | 所属部门     |
| email          | varchar(20)                                                  | varchar  | 20   | YES      |        | 邮箱         |
| endContract    | date                                                         | date     |      | YES      |        | 合同终止日期 |
| engageForm     | varchar(8)                                                   | varchar  | 8    | YES      |        | 聘用形式     |
| gender         | char(4)                                                      | char     | 4    | YES      |        | 性别         |
| id             | int(11)                                                      | int      |      | NO       |        | 员工编号     |
| idCard         | char(18)                                                     | char     | 18   | YES      |        | 身份证号     |
| jobLevelId     | int(11)                                                      | int      |      | YES      |        | 职称ID       |
| name           | varchar(10)                                                  | varchar  | 10   | YES      |        | 员工姓名     |
| nationId       | int(8)                                                       | int      |      | YES      |        | 民族         |
| nativePlace    | varchar(20)                                                  | varchar  | 20   | YES      |        | 籍贯         |
| notWorkDate    | date                                                         | date     |      | YES      |        | 离职日期     |
| phone          | varchar(11)                                                  | varchar  | 11   | YES      |        | 电话号码     |
| politicId      | int(8)                                                       | int      |      | YES      |        | 政治面貌     |
| posId          | int(11)                                                      | int      |      | YES      |        | 职位ID       |
| school         | varchar(32)                                                  | varchar  | 32   | YES      |        | 毕业院校     |
| specialty      | varchar(32)                                                  | varchar  | 32   | YES      |        | 所属专业     |
| tiptopDegree   | enum('博士','硕士','本科','大专','高中','初中','小学','其他') | enum     | 2    | YES      |        | 最高学历     |
| wedlock        | enum('已婚','未婚','离异')                                   | enum     | 2    | YES      |        | 婚姻状况     |
| workAge        | int(11)                                                      | int      |      | YES      |        | 工龄         |
| workID         | char(8)                                                      | char     | 8    | YES      |        | 工号         |
| workState      | enum('在职','离职')                                          | enum     | 2    | YES      | 在职   | 在职状态     |




employeeec表（员工奖励惩罚表）



| 列名     | 数据类型     | 字段类型 | 长度 | 是否为空 | 默认值 | 备注                   |
| -------- | ------------ | -------- | ---- | -------- | ------ | ---------------------- |
| ecDate   | date         | date     |      | YES      |        | 奖罚日期               |
| ecPoint  | int(11)      | int      |      | YES      |        | 奖罚分                 |
| ecReason | varchar(255) | varchar  | 255  | YES      |        | 奖罚原因               |
| ecType   | int(11)      | int      |      | YES      |        | 奖罚类别，0：奖，1：罚 |
| eid      | int(11)      | int      |      | YES      |        | 员工编号               |
| id       | int(11)      | int      |      | NO       |        |                        |
| remark   | varchar(255) | varchar  | 255  | YES      |        | 备注                   |








































