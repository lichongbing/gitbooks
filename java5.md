# Java基础

<a id="2"></a>
### Java 开发环境搭建
过上一章的阅读，相信读者对Java语言已经有了大概的了解，本章更进一步地介绍如何在Windows操作系统中下载与安装JDK，并详细描述在Windows操作系统下开发环境的配置。最后介绍如何编译和运行第1个Java程序，再简要介绍在Eclipse环境下如何开发Java程序。
本章要点（已掌握的在方框中打钩）

* 掌握下载、安装Java开发工具箱

* 掌握开发环境变量的配置

* 学会编写第1个Java程序

* 学会在Eclipse下编写Java程序
<a id="21"></a>
#### 1.1 Java开发环境

学习Java的第一步，自然就是要搭建Java开发环境（Java Development Kit，JDK），在操作系统（如Windows、Linux等）下，JDK是搭建Java最基本的开发环境之一，目前由Oracle公司维护开发并免费提供。DK由一个处于操作系统层之上的开发环境和运行环境组成，如下图所示。JDK除了包括编译（javac）、解释（java）、打包（jar）等工具，还包括开发工具及开发工具的应用程序接口等。当Java程序编译完毕后，如果想运行，还需要Java运行环境（Java Runtime Environment，JRE）。JRE是运行Java程序所必需的环境的集合，包含JVM标准实现及Java核心类库。如果仅仅想运行Java程序，安装JRE就够了。也就是说，JRE是面向Java程序的使用者的。但如果想进一步开发Java程序，那就需要安装JDK，它是面向Java程序的开发者的。Java程序的开发者自然也是Java程序的应用者。从下图也容易看出，JDK包含JRE。

由上图可以看出，Java程序开发的第一步就是编写Java语言的源代码。而编写源代码的工具，可以是任何文本编辑器，如Windows 操作系统下的记事本、Linux操作系统下的Vim等。这里推荐读者使用对编程语言支持较好的编辑器，如Notepad++、UltraEdit、Editplus等，这类代码编辑器通常有较好的语法高亮等特性，特别适合开发程序代码。Java源文件编写完毕后，就可以在命令行下，通过javac命令将Java源程序编译成字节码（Byte Code，Java虚拟机执行的一种二进制指令格式文件)，然后通过java命令，来解释执行编译好的Java类文件（文件扩展名为.class）。但如果想正确使用javac和java等命令，用户必须自己搭建Java开发环境。在后续章节，我们将详细介绍相关的配置步骤。为了提高Java的开发效率，目前在市面上也涌现了很多优秀的Java集成开发环境（Integrated Development Environment， IDE），如NetBeans（由Sun公司开发的老牌IDE）、IntelliJIDEA（由捷克软件公司JetBrains开发的智能IDE，需要付费使用）及Eclipse（免费开源的知名IDE）等。IDE在JDK的基础上，为程序提供了很多辅助功能的支持，极大方便了程序的开发。在本章最后部分，我们将简要地介绍最流行的 IDE之一——Eclipse的使用。
<a id="22"></a>
#### 1.2 安装Java开发工具箱

Oracle公司提供多种操作系统下的不同版本的JDK。本节主要介绍在Windows操作系统下安装JDK的过程。
###### 1.2.1 下载JDK
但需要提醒读者的是，对于软件开发而言，过度“最新”并非好事，如果你不是有特殊需求，Java 8足够用了。为什么说过度“最新”并非好事呢？这是因为Java 9和Java 10虽然有很多好的新特性，但它依附的生态还没有建立起来。比如说，如果你想学习基于Hadoop的大数据编程，很可能Hadoop的最新版还是由Java 8编译而成，你用Java 10编译出来的程序，难以在Hadoop上运行。所以对于学习编程软件，特别是初学者，我们的建议是保守的，暂时还采用业界广泛使用的Java来编程。事实上，Java 8、 Java 7甚至Java 6，仍在企业界有着广泛应用。作为初级用户，实在没有必要跟风，一定要下载最新的Java版本，因为很多新特性，初学者根本没有机会用到。或许Oracle公司也知Java 9和Java 10的更新幅度太大，而Java 8依然是业界开发的主流，于是，在Java 10 同一个下载网页的下方，Oracle给出了Java 8的下载界面，如下图所示。