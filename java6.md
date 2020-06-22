<a id="3"></a>
## 初识庐山真面目——Java程序要素概览
>麻雀虽小，五脏俱全。本章的实例虽然非常简单，但基本涵盖了本篇所讲的内容。可以通过本章来了解Java程序的组成及内部部件（如Java中的标识符、关键字、变量、注释等）。同时，本章还涉及Java程序错误的检测及Java编程风格的注意事项。

本章要点（已掌握的在方框中打钩）
* 掌握Java程序的组成
* 掌握Java程序注释的使用
* 掌握Java中的标识符和关键字
* 了解Java中的变量及其设置
* 了解程序的检测
* 掌握提高程序可读性的方法

### 2.1 一个简单的例子

从本章开始，我们正式开启学习Java程序设计的旅程。在本章，除了认识程序的架构外，我们还将介绍标识符、关键字以及一些基本的数据类型。通过简单的范例，让读者了解检测与提高程序可读性的方法，以培养读者良好的编程风格和正确的程序编写习惯。

下面来看一个简单的Java程序。在介绍程序之前，读者先简单回顾一下第1章讲解的例子，之后再来看下面的这个程序，在此基础上理解此程序的主要功能。

```
/**
 
   * @ClassName: TestJava
  
   * @Description: 这是Java的一个简单范例
  
   * @author: YuHong 
  
   * @date: 2016年11月15日 
 
   */
  public class TestJava
 {
    public static void main(String args[ ])
    {
    int num ;  // 声明一个整型变量num
    num = 5 ;  // 将整型变量赋值为5
    // 输出字符串，这里用“+” 号连接变量
      System.out.println("这是数字 " + num); 
     System.out.println("我有 " + num + "本书！");
   }
 }
```