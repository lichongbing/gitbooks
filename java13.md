# 凝练才是美——抽象类、接口与内部类


>抽象类、接口和内部类为我们提供了一种将接口与实现分离的更加结构化的方法。正是由于这些机制的存在，才赋予Java强大的面向对象的能力。本章讲述抽象类的基本概念、具有多继承特性的接口和内部类。

本章要点（已掌握的在方框中打钩）
>熟悉抽象类的使用

>掌握抽象类的基本概念

>掌握抽象类实例的应用

>掌握接口的基本概念

>熟悉Java 8中接口的新特性

>熟悉接口实例的应用

>熟悉内部类的使用

在前面的章节中，我们反复强调一个概念：在Java面向对象编程领域，一切都是对象，并且所有的对象都是通过“类”来描述的。但是，并不是所有的类都是来描述对象的。如果一个类没有足够的信息来描述一个具体的对象，还需要其他具体的类来支撑它，那么这样的类我们称为抽象类。比如new Person( )，但是这个“人类”——Person( )具体长成什么样子，我们并不知道。他/她没有一个具体人的概念，所以这就是一个抽象类，需要一个更为具体的类，如学生、工人或老师类，来对它进行特定的“具体化”，我们才知道这人长成啥样。
<a id="1"></a>
## 9.1 抽象类

### 9.1.1 抽象类的定义

Java中有一种类，派生出很多子类，而自身是不能用来产生对象的，这种类称为“抽象类”。抽象类的作用有点类似于“模板”，其目的是要设计者依据它的格式来修改并创建新的子类。

抽象类实际上也是一个类，只是与之前的普通类相比，内部新增了抽象方法。所谓抽象方法，就是只声明而未实现的方法。所有的抽象方法必须使用abstract关键字声明，而包含抽象方法的类就是抽象类，也必须使用abstract class声明。

抽象类定义规则如下。抽象类和抽象方法都必须用abstract关键字来修饰。抽象类不能直接实例化，也就是不能直接用new关键字去产生对象。在抽象类中定义时抽象方法只需声明，而无需实现。含有抽象方法的类必须被声明为抽象类，抽象类的子类必须实现所有的抽象方法后，才能不叫抽象类，从而可以被实例化，否则这个子类还是个抽象类。
```java
abstract class 类名称　　　　　　// 定义抽象类
{　 声明数据成员 ；
　 访问权限 返回值的数据类型 方法名称（参数…）
　 {　　　
     // 定义一般方法
　  ｝　 
abstract 返回值的数据类型 方法名称（参数…）；　 
// 定义抽象方法，在抽象方法里没有定义方法体　
}
```
例如以下形式。
```java
abstract class Book　　　　　　// 定义一个抽象类
{　　 
    private String title = "Java开发" ; // 属性　 
    public void print()　 
    {　　　　　　　　　
         // 普通方法，用“{}”表示有方法体　　 
          System.out.println(title) ;　 
          }
 　 public abstract void fun() ;
 　　  // 没有方法体，是一个抽象方法
 }
 ```

由上例可知，抽象类的定义只是比普通类多了一些抽象方法的定义而已。虽然定义了抽象类，但是抽象类却不能直接使用。
```java
   Book book = new Book() ;　　// 错误: Book是抽象的; 无法实例化
```   
### 9.1.2 抽象类的使用


如果一个类可以实例化对象，那么这个对象可以调用类中的属性或方法，但是抽象类中的抽象方法没有方法体，没有方法体的方法无法使用。

所以，对于抽象类的使用原则如下。

>抽象类必须有子类，子类使用extends继承抽象类，一个子类只能够继承一个抽象类。

>产生对象的子类，则必须实现抽象类之中的全部抽象方法。也就是说，只有所有抽象方法不再抽象了，做实在了，才能依据类（图纸），产生对象（具体的产品）。

>如果想要实例化抽象类的对象，则可以通过子类进行对象的向上转型来完成。


## 提示

在Java中，当子类继承父类时，子类可由此得到父类的方法。但不愿“墨守成规”的子类，可在子类中重新改写继承于父类的同名方法，我们称这个过程为覆盖重写，简称覆写（override）。

从抽象类的设计理念可知，抽象类生来就是被继承的。在其内的抽象方法通常是没有方法体的，因为有了也没用，抽象方法的本意就是期望其“子孙后代”类重新定义这个方法，并赋予新的内涵。这样一来，虽然在Java英文文档中依然用“override”来表明子类重新定义来自父类的抽象方法，但如果还将“override”翻译为“覆写”，就达不到“信达雅”的要求。

六祖惠能大师有句名言：“本来无一物，何处惹尘埃。”

在这里，我们也可说一句：“本无方法体，何处来覆写。”

因此，在本书中，对抽象类和接口中的抽象方法，在其子类中给予具体定义时，我们用“实现”而非“覆盖”来描述这个过程。用“实现”，相当于在子类中，将来自父类的抽象方法“给予”生命。这样可能更有韵意。

范例9-1 抽象类的用法案例（AbstractClassDemo.java）

```java
　abstract class Person　　  //定义一抽象类Person
　{
　　 String name ;
　　 int age;
　　 String occupation ;　
　　 public abstract String talk( ) ; // 声明一抽象方法talk( )
　}  
　class Student extends Person　 // Student类继承自Person类
　{
　　 public Student(String name,int age,String occupation)
　　 {
　　　this.name = name ;
　　　this.age = age ;
　　　this.occupation = occupation ;
　　 }
　　 
　　 @Override
　　 public String talk( )　// 实现talk( )方法
　　 {
　　　return "学生——&gt;姓名：" + name+"，年龄：" + age+"，职业：" + occupation ;
　　 }
　}
　class Worker extends Person　 // Worker类继承自Person类
　{
　　 public Worker(String name,int age,String occupation)
　　 {
　　　 this.name = name ;
　　　 this.age = age ;
　　　 this.occupation = occupation ;
　　 }
　　 public String talk()　  // 实现talk( )方法
　　 {
　　　 return "工人——&gt;姓名：" + name + ",年龄：" + age  + ",职业:" + occupation ;
　　 }
　}
　public class AbstractClassDemo
　{
　　 public static void main(String[] args) 
　　 {
　　　 Student s = new Student("张三",20,"学生"); //创建Student类对象s
　　　 Worker w = new Worker("李四",
,"工人");  //创建Worker类对象w
　　　 System.out.println(s.talk( )) ;　　　 //调用被实现的方法
　　　 System.out.println(w.talk( )) ;
　　 }
　}
```

程序运行结果如下图所示。

代码详解

第01~07行声明了一个名为Person的抽象类，在Person中声明了3个属性和一个抽象方法——talk( )。

第08~22行声明了一个Student类，此类继承自Person类，因为此类不为抽象类，所以需要“实现”Person类中的抽象方法——talk( )。

类似的，第23~35行声明了一个Worker类，此类继承自Person类，因为此类不为抽象类，所以需要“实现”Person类中的抽象方法——talk( )。

第40行和第41行分别实例化Student类与Worker类的对象，并调用各自的构造方法初始化类属性。

因为Student类与Worker类继承自Person类，所以Person类的数据成员name、age和occupation，也会自动继承到Student类与Worker类。

因此这两个类的构造方法，需要初始化这3个数据成员。第42行和第43行分别调用各自类中被实现的talk( )方法

【范例分析】可以看到Student和Worker两个子类都分别按各自的要求，在子类实现了talk( )方法。上面的程序可由下图表示。抽象类的特征如下所示。

（1）抽象类中可以拥有构造方法。

与一般类相同，抽象类也可以拥有构造方法，但是这些构造方法必须在子类中被调用，并且子类实例化对象的时候依然满足类继承的关系，先默认调用父类的构造方法，而后再调用子类的构造方法，毕竟抽象类之中还是存在属性的，但抽象类的构造方法无法被外部类实例化对象调用。

范例9-2 抽象类中构造方法的定义使用（AbstractConstructor.java）
```java
　 abstract class Person　　　　　　　　　//定义一抽象类Person
　{
　　String name ;　　  
　　int age ;
　　String occupation ;
　　public Person(String name,int age,String occupation)  //定义构造函数
　　{
　　　this.name = name ;
　　　this.age = age ;
　　　this.occupation = occupation ;
　　}
　　 public abstract String talk() ;　 //声明一个抽象方法
　 }
　class Student extends Person　　//声明抽象类的子类
　{
　　public Student(String name,int age,String occupation)　 
　　{  // 在这里必须明确调用抽象类中的构造方法
　　　super(name,age,occupation);
　　}
　　public String talk()　　　　  // 实现talk()方法
　　{
　　return "学生——&gt;姓名：" + name + "，年龄：" + age + "，职业：" + occupation;
　　}
  }
　class AbstractConstructor
　{
　　public static void main(String[] args) 
　　{
　　　Student s = new Student("张三",18,"学生") ;//创建对象s
　　　System.out.println(s.talk()) ;  //调用实现的方法
　　}
　}
```
保存并运行程序，结果如下图所示。

代码详解第01~13行声明了一个名为Person的抽象类，在Person中声明了3个属性、一个构造函数和一个抽象方法——talk( )。

第14~24行声明了一个Student类，此类继承自Person类，因为此类不为抽象类，所以需要在子类中实现Person类中的抽象方法——talk( )。

第18行，使用super( )方法，显式调用抽象类中的构造方法。

第29行实例化Student类，建立对象s，并调用父类的构造方法初始化类属性。

第30行调用子类中实现的talk( )方法。

【范例分析】从程序中可以看到，抽象类也可以像普通类一样，有构造方法、一般方法和属性，更重要的是还可以有一些抽象方法，需要子类去实现，而且在抽象类中声明构造方法后，在子类中必须明确调用。

（2）抽象类不能使用final定义，因为使用final定义的类不能有子类，而抽象类使用的时候必须有子类，这是一个矛盾的问题，所以抽象类上不能出现final定义。

（3）抽象类之中可以没有抽象方法，但即便没有抽象方法的抽象类，其“抽象”的本质不会发生变化，所以也不能够直接在外部通过关键字new实例化。
<a id="2"></a>
## 9.2 接口

9.2.1 接口的基本概念

对C语言有所了解的读者就会知道，在C语言中，有种复合的数据类型——structure（结构体），结构体可视为纯粹是把一系列相关数据汇集在一起（the collections of data），比如说，我们可以把“班级”“学号”“姓名”“性别”“成绩”等数据属性，构成一个名为“学生”的结构体。

Java提供了一种机制，把对数据的通用操作（也就是方法），汇集在一起（the collections of common operation），形成一个接口（interface），以形成对算法的复用。

所谓算法，就是一系列相关操作指令的集合。

接口，是Java所提供的另一种重要技术，它可视为一种特殊的类，其结构和抽象类非常相似，是抽象类的一种变体。

在Java 8之前，接口的一个关键特征是，它既不包含方法的实现，也不包含数据。

换句话说，接口内定义的所有方法，都默认为abstract，即都是“抽象方法”。

现在，在Java 8中，接口的规定有所松动，它内部允许包括数据成员，但这些数据必须是常量，其值一旦被初始化后，是不允许更改的，这些数据成员通常为全局变量。

所以，当我们在一个接口定义一个变量时，系统会自动把“public ”“static”“final”这3个关键字添加在变量前面，如以下代码所示。

public interface faceA{　 int NORTH = 1;}上面的代码等效为以下代码。

public interface faceA{　public static final int NORTH = 1;}接口的设计宗旨在于，定义由多个继承类共同遵守的 “契约”。

所以接口中的所有成员，其访问类型都必须为public，否则不能被继承，就失去了“契约”内涵。

为了避免在接口中添加新方法后而要修改所有实现类，同时也是为了支持Lambda新特性的引入，从JDK 8开始，Java的接口也放宽了一些限制，接口中还可以“有条件”地对方法进行实现。

例如，允许定义默认方法（即default方法），也可称为Defender方法。

default方法是指，允许在接口内部实现一些默认方法（也就是说，在接口中可以包含方法体，这打破了Java 8版本之前对接口的语法限制），从而使得接口在进行扩展的时候，不会破坏与接口相关的实现类代码。

在Java中使用interface关键字来定义一个接口。

接口定义的语法如下所示。

interface 接口名称　// 定义接口{　 final 数据类型 成员名称 = 常量 ；　// 数据成员必须赋初值　 abstract 返回值的数据类型 方法名称（参数…）；// 抽象方法，抽象方法没有方法体　 default  返回值的数据类型 方法名称（参数…）// 默认方法，包含方法体　 {　　  …方法体…　 }}接口的定义范例如下所示。
```java
interface B  // 定义一个接口B
{　　 
    public static final String INFO = "Hello World ." ;　// 全局常量，public、static、final可省略　 
    public abstract void print() ;　　　　　　 // 抽象方法　 
    default public void otherprint()　　　　　// 带方法体的默认方法　 
    {　　　　  　　  
        System.out.println("default methods!");　　　//默认方法的方法体　 
    }
}
```
虽然定义了接口，但在所定义的接口A和接口B中，因接口内存在抽象方法，因此这些接口都不能被用户直接使用，必须在其子类中“实现”这些抽象方法，把“抽象的”方法“务实”了，变为实实在在的可用方法，才可以用之实例化对象。

9.2.2 使用接口的原则使用接口时，注意遵守如下原则。

接口必须有子类，子类依靠implements关键字可以同时实现多个接口。

接口的子类（如果不是抽象类）必须实现接口之中的全部抽象方法，才能实例化对象。

利用子类实现对象的实例化，接口可以实现多态性。

接口与一般类一样，本身也拥有数据成员与方法，但数据成员一定要赋初值，且此值不能再更改，方法也必须是“抽象方法”或default方法。

也正因为接口内的方法除default方法外必须是抽象方法，而没有其他一般的方法，所以在接口定义格式中，声明抽象方法的关键字abstract是可以省略的。

同理，因接口的数据成员必须赋初值，且此值不能再被更改，所以声明数据成员的关键字final也可省略。

简写的接口定义范例如下。
```java
interface A  // 定义一个接口
{　　 
    public static String INFO = "Hello World ." ;　// 全局常量　 
    public void print() ;　　　　　　　 // 抽象方法　 
    default public void otherprint()　 
    {　　　　　　　　　　　 
        // 带方法体的默认方法　　  
        System.out.println("default methods!");　　 
    }
}
```
在Java中，由于禁止多继承（通俗来讲，就好比一个“儿子”只能认一个“老爸”），而接口做了一点变通，一个子类可以“实现”多个接口，实际上，这是“间接”实现多继承的一种机制，这也是Java设计中的一个重要环节。

既然接口中除了default方法，只能有抽象方法，所以这类方法只需声明，而无需定义具体的方法体，于是自然可以联想到，接口没有办法像一般类一样，用它来创建对象。

利用接口创建新类的过程称为接口的实现（implementation）。

以下为接口实现的语法。

```java
class 子类名称 implements 接口A,接口B…    // 接口的实现{…}范例9-3 带default方法接口的实现（Interfacedefault.java）
　interface InterfaceA　　　　　　　　　　// 定义一个接口
　{　
　　 public static String INFO = "static final." ; // 全局常量
　　 public void print( ) ;　　　　　　　　// 抽象方法
　　 
　　 default public void otherprint( )　　　　  // 带方法体的默认方法
　　 {
　　　  System.out.println("print default1 methods InterfaceA!");
　　 }
　}
　
　class subClass implements InterfaceA　　  //子类InterfaceA实现接口InterfaceA
　{
　　 public void print( )　　　　　　  //实现接口中的抽象方法print( )
　　 {
　　　  System.out.println("print abstract methods InterfaceA!");
　　　  System.out.println(INFO);  
　　 }
　}
　public class Interfacedefault 
　{
　　 public static void main(String[ ] args) 
　　 {
　　　  subClass subObj = new subClass( );　　  //实例化子类对象
　　　  subObj.print( );　　　　　　　  //调用“实现”过的抽象方法
　　　  subObj.otherprint( );　　　　　　 //调用接口中的默认方法
　　　  System.out.println(InterfaceA.INFO);　　//输出接口中的常量
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解第01~10行定义接口InterfaceA，其中定义全局静态变量INFO、抽象方法print()及默认方法otherprint()。

第12~19行定义子类subClass，实现接口InterfaceA，“实现”从接口InterfaceA继承而来的方法print()。

第24行实例化子类对象，并调用在子类实现的抽象方法（第25行）和默认方法（第26行），输出接口InterfaceA的常量INFO（第27行）。

【范例分析】上例中定义了一个接口，接口中定义常量INFO，省略了关键词final，定义抽象方法print()；，也省略了Abstract，定义带方法体的默认方法。

第17行和第27行分别引用接口中的常量。

在Java 8中，允许在一个接口中只定义默认方法，而没有一个抽象方法，下面举例说明。

范例9-4 仅有default方法接口的使用（InterfacedefaultOnly.java）
```java
　interface InterfaceA　　　　　　　 // 定义一个接口
　{　
　　 default public void otherprint( )　　// 带方法体的默认方法
　　 {
　　　  System.out.println("print default1 methods only in InterfaceA!");
　　 }
　}
　class subClass implements InterfaceA　　 //子类subClass实现接口InterfaceA
　{　
　　 //do nothing
　}
　public class InterfaceDefaultOnly 
　{
　　 public static void main(String[ ] args) 
　　 {
　　　  subClass subObj = new subClass( );　//实例化子类对象　
　　　  subObj.otherprint();　　　　　　 //调用接口中的默认方法　　  
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解第01~07行定义接口InterfaceA，其中定义默认方法otherprint()。

第08~11行定义子类subClass，实现接口InterfaceA。

第16~17行实例化子类对象subObj，并调用由接口InterfaceA继承而来的默认方法otherprint()。

【范例分析】由于接口InterfaceA中并无抽象方法，因此无抽象方法需要在子类中“实现”，所以子类subClass的主体部分什么也没有做，但这部分的工作是必需的，因为接口是不能（通过new操作）实例化对象的，即使子类subClass什么也没有做，其实也实现了一个功能，即由subClass可以实例化对象。

接口与抽象类相比，主要区别就在于子类上，子类的继承体系中，永远只有一个父类，但子类却可以同时实现多个接口，变相完成“多继承”，如下例所示。

范例9-5 子类继承多个接口的应用（InterfaceDemo.java）

```java
　interface faceA　 // 定义一个接口
　{  
　　 public static final String INFO = "Hello World!" ; // 全局常量
　　 public abstract void print( ) ;  // 抽象方法
　}
　interface faceB　  // 定义一个接口
　{　
　　 public abstract void get( ) ;
　}
　class subClass implements faceA,faceB 
　{　 // 一个子类同时实现了两个接口
　　 public void print( ) 
　　 {
　　　  System.out.println( INFO ) ;
　　 }
　　 public void get( ) 
　　 {
　　　  System.out.println("你好！") ;
　　 }
　}
　public class InterfaceDemo  
　{
　　 public static void main(String args[]) 
　　 {
　　　  subClass subObj = new subClass() ; // 实例化子类对象
　　　  
　　　  faceA fa = subObj ;　// 为父接口实例化
　　　  fa.print() ;
　　　  
　　　  faceB fb = subObj ;　// 为父接口实例化
　　　  fb.get() ;
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解第01~05行定义接口faceA，其中定义全局变量INFO和抽象方法print()。

第06~09行定义接口faceB，并定义了抽象方法get( )。

第10~20行定义子类subClass，同时实现接口faceA和faceB，并分别对接口faceA和faceB中的抽象方法进行实现。

【范例分析】由上例可以发现接口与抽象类相比，主要区别就在于子类上，子类可以同时实现多个接口。

但在Java 8中，如果一个类实现两个或多个接口，即“变相”的多继承，但是若其中两个接口中都包含一个名字相同的default方法，如下例中的faceA和faceB中有同名的默认方法DefaultMethod( )，但方法体不同。

范例9-6 同时实现含有两个相同默认方法名的接口（Interfacsamedefaults.java）
```java
　interface faceA　　　　　　 //定义接口faceA
　{　
　　 void someMethod( );
　　 default public void DefaultMethod( )//定义接口中的默认方法
　　 {
　　　  System.out.println("Default method in the interface A");
　　 }
　}
　interface faceB　　　　　　 //定义接口faceB
　{  
　　 default public void DefaultMethod( )//定义接口InterfaceB中同名的默认方法
　　 {
　　　  System.out.println("Default method in the interface B"); 
　　 }
　}
　class DefaultMethodClass implements faceA,faceB  //子类同时实现接口faceA和faceB
　{　public void someMethod( )　　　　　 //实现接口InterfaceA的抽象方法
　　{
　　　  System.out.println("Some method in the subclass");　
　　 }　
　}
　public class Interfacsamedefaults 
　{　
　　 public static void main(String[] args)
　　 {　
　　　  DefaultMethodClass def = new DefaultMethodClass( );
　　　  def.someMethod();　　　　 //调用抽象方法
　　　  def.DefaultMethod();　　　　//调用默认方法
　　 }
　}
```
保存程序并运行，编译并不能通过，如下图所示。

代码详解代码第01~08行定义了一个接口faceA，其中定义抽象方法someMethod( )和默认方法DefaultMethod( )，请注意，someMethod( )前面的public和abstract关键字可以省略，这是因为在接口内的所有方法（除了默认类型方法），都是“共有的”和“抽象的”，所以这两个关键字即使省略了，“智能”的编译器也会替我们把这两个关键字加上。

代码第09~15行定义了另外一个接口faceB，其中定义了一个和接口faceA同名的默认方法DefaultMethod( )，其实这两个默认方法的实现部分并不相同。

第16~21行定义了子类DefaultMethodClass，同时实现接口faceA和faceB，并对接口faceA 中的抽象方法someMethod( )给予实现。

代码第26行，实例化子类DefaultMethodClass的对象。

【范例分析】如果编译以上代码，编译器会报错，因为在实例化子类DefaultMethodClass的对象时，编译器不知道应该在两个同名的default方法——DefaultMethod中选择哪一个（Duplicate default methods named DefaultMethod），因此产生了二义性。

因此，一个类实现多个接口时，若接口中有默认方法，不能出现同名默认方法。

事实上，Java之所以禁止多继承，就是想避免类似的二义性。

但在接口中允许实现默认方法，似乎又重新开启了“二义性”的灾难之门。

在“变相”实现的多继承中，如果说在一个子类中既要实现接口，又要继承抽象类，则应该采用先继承后实现的顺序完成。

范例9-7 子类同时继承抽象类，并实现接口（ExtendsInterface.java）
```java
　interface faceA 
　{　 // 定义一个接口
　　 String INFO = "Hello World." ;
　　 void print( ) ;  // 抽象方法
　}
　interface faceB 
　{　// 定义一个接口
　　 public abstract void get( ) ;
　}
　abstract class abstractC 
　{  // 抽象类
　　 public abstract void fun( ) ;　 // 抽象方法
　}
　class subClass extends abstractC implements faceA,faceB 

　{  // 先继承后实现
　　 public void print( ) 
　　 {
　　　  System.out.println(INFO) ;
　　 }
　　 public void get( ) 
　　 {
　　　  System.out.println("你好！") ;
　　 }
　　 public void fun( ) 
　　 {
　　　  System.out.println("你好！JAVA") ;
　　 }
　}
　public class ExtendsInterface
　{
　　 public static void main(String args[]) 
　　 {
　　　  subClass subObj = new subClass( ) ; // 实例化子类对象
　　　  faceA fa = subObj ;　// 为父接口实例化
　　　  faceB fb = subObj ;　// 为父接口实例化
　　　  abstractC ac = subObj ;　// 为抽象类实例化
　
　　　  fa.print() ;
　　　  fb.get() ;
　　　  ac.fun();
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解第01~05行声明了一个接口faceA，然后在里面声明了1个常量INFO并赋初值"Hello World."，同时定义了一个抽象方法print( )。

第06~09行声明了一个接口faceB，在其内定义了一个抽象方法get()。

第10~13行声明抽象类abstractC，在其内定义了抽象方法fun()。

第14~28行声明子类subClass，它先继承（extends）抽象类B，随后实现（implements）接口faceA和faceB。

第33行实例化了子类subClass的对象subObj。

第34~35行实现父接口实例化。

第36行实现抽象类实例化。

【范例分析】如果我们非要“调皮地”把第14行代码，从原来的“继承在先，实现在后”，如下所示。

class subClass extends abstractC implements faceA,faceB改成“实现在先，继承在后”，如下所示。

class subClass implements faceA,faceB extends abstractC编译器是不会答应的，它会报错，如下图所示。

9.2.3 接口的作用——Java的回调机制回调（callback）是Java中很重要的一个概念，在后面章节讲解的Spring、Hibernate等计算框架中，都大量使用了回调技术，所以有必要了解一下这个机制。

在设计模式中，有个较新的模式，叫控制反转（Inversion of Control，IoC），它是一个重要的面向对象编程的法则，用来削减计算机程序的耦合问题，也是轻量级的Spring框架的核心。

由于概念相对较新，在Erich Gamma等四人组合著的《Design Patterns》（设计模式）中，并没有体现这一模式。

控制反转的本质，就是Java中的回调机制。

“回调”，其英文“call back”的原意是“回电话”，这最早源于“好莱坞原则（Hollywood principle）”：“Don't call me, we will callyou（不要给我打电话，我们会打给你）”。

也就是说，如果好莱坞明星想演节目，不用自己去找好莱坞公司，而是由好莱坞公司主动去找他们（当然，之前这些明星必须要在好莱坞登记过）。

言外之意，虽然我们之间有通电话的需求，但是我们会在需要的时候，再确定下来通电话的对象。

在某些面向过程（事件驱动）的编程语言（如C语言）中，开发人员可以通过传递函数指针（function pointer）直接实现回调机制，回调的对象可能是一段代码块（方法块）。

但Java作为一门面向对象的编程语言，并不支持方法指针（method pointer，在Java中，方法的地位等同于C中的函数），所以想实现回调机制，必须通过“对象（object）”来完成，这似乎妨碍了回调机制的完成。

Java“关上了一扇门，必然会为你开启另一扇窗”，而这扇窗就是“接口”。

在Java中，回调流程通常要从声明一个接口开始。

下面我们举例说明。

范例9-8 Java回调机制的演示（Caller.java）
```java
　interface CallBack 
　{
　　 void methodToCallBack( );
　}
　class CallBackImpl implements CallBack 
　{
　　 public void methodToCallBack( ) 
　　 {
　　　  System.out.println("I'"ve been called back");
　　 }
　}
　public class Caller 
　{
　　 public void register(CallBack callback) 
　　 {
　　　  callback.methodToCallBack( );
　　 }
　　 public static void main(String[] args) 
　　 {
　　　  Caller caller = new Caller( );
　　　  CallBack callBack = new CallBackImpl( );
　　　  caller.register(callBack);
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解第01~04行，声明了一个接口CallBack，在这个接口中声明了一个抽象方法methodToCallBack( )。

第05~11行，用一个名为CallBackImpl的类，实现了接口CallBack。

第12~24行，设计了一个主调类Caller，其中第14~17行声明了一个注册方法register()，特别需要注意的是，这个方法的参数是接口对象CallBack的引用。

第20行，新建了一个Caller对象，第21行新建了一个CallBackImpl的对象，它是接口CallBack的具体实现者。

第22行，调用注册方法register()，实参就是CallBackImpl的对象callBack，因为CallBackImpl实现（某种程度上可以说是继承）了抽象接口，所以在register()方法中，callBack可以调用methodToCallBack()方法。

或许，读者会困惑，为什么不在第21行之后这么做。

callback.methodToCallBack()这样岂不是更加简便？的确如此。

但这段代码不在于如何用最短的代码实现具体功能，而是为了给我们展示一下，如何在Java环境下实现一个回调机制。

我们知道，回调机制的真正意图，其实是为了实现“控制反转（Inversion of Control）”。

通过控制反转，对象在被创建的时候（如第21行），由一个能够调控系统内所有对象的外界实体（如第20行的caller），将其所依赖的对象的引用传递给功能方法块（如第22行的callBack，被送入到register()中）。

我们知道，同一个接口，可以有不同的实现类，从而使得这些不同的实现类，可以定义众多不同的对象，而这些对象会被按需“注入”功能方法块register()。

在被调用前，这些对象永远处于等待调用状态，直到有一天被回调（callback）。

由上分析可知，控制反转可以用来降低计算机代码之间的耦合度。

在控制反转的设计模式提出之后，引起了很大的关注和争议。

于是，资深程序员马丁 ● 福勒（Martin Fowler）发表了一篇经典文章《Inversionof Control Containers and the Dependency Injection pattern》（控制容器的反转和依赖注入模式），终于算是平息了争论。

于是，“控制反转”又获得了一个新的名字：“依赖注入 （Dependency Injection）”。

“依赖注入”的确更加准确地描述了这种设计理念。

所谓依赖注入，就是指组件之间的依赖关系由容器在运行期决定，在注入之前，对象之间的耦合关系是松散的。

下面，我们再列举一个更加实用的案例，来说明Java中的回调机制。

范例9-9 利用接口实现Java中的回调机制（callBackDemo.java）
```java
　import java.awt.Rectangle;
　interface Measurer
　{
　　 double measure(Object anObject); 
　}
　class AreaMeasurer implements Measurer 
　{
　　 public double measure(Object anObject) 
　　 {
　　　  Rectangle aRectangle = (Rectangle) anObject;
　　　  double area = aRectangle.getWidth() * aRectangle.getHeight(); 
　　　  return area;
　　 } 
　}
　class Car 
　{  
　　 private double price;
　　 private double taxRate;
　　 Car(double price, double taxRate)
　　 {
　　　  this.price = price;
　　　  this.taxRate = taxRate;
　　 }
　　 public double getPrice()
　　 {
　　　  return price;
　　 }
　　 public double getRate()
　　 {
　　　  return taxRate;
　　 }
　}
　class CarMeasurer implements Measurer 
　{
　　 public double measure(Object anObject) 
　　 {
　　　  Car aCar = (Car) anObject;
　　　  double totalPrice = aCar.getPrice() * (1 + aCar.getRate()); 
　　　  return totalPrice;
　　 } 
　}
　class Data
　{
　　 public static double average(Object[] objects, Measurer meas) 
　　 {
　　　  double sum = 0.0;
　　　  for (Object obj : objects)
　　　  {
　　　　　sum = sum + meas.measure(obj); 
　　　  }
　　　  if (objects.length &gt; 0) 
　　　  {
　　　　　return sum / objects.length; 
　　　  } else { 
　　　　　return 0;
　　　  } 
　　 }
　}
　public class callBackDemo
　{
　　 public static void main(String[] args) 
　　 {
　　　  Measurer areaMeas = new AreaMeasurer(); 
　　　  Rectangle[] rects = new Rectangle[]
　　　  {
　　　　　new Rectangle(5, 
, 
, 
), 
　　　　　new Rectangle(
, 
, 
, 
),
　　　　　new Rectangle(
, 
, 5, 
)
　　　  }; 
　　　  double averageArea = Data.average(rects, areaMeas); 
　　　  System.out.println("平均面积为: " + averageArea); 
　　　　　　 
　　　  Measurer carMeas = new CarMeasurer(); 
　　　  Car[] cars = new Car[]
　　　  {
　　　　　new Car(

0, 0.
), 
　　　　　new Car(

0, 0.
), 
　　　　　new Car(

0, 0.
), 
　　　  }; 
　　　  double averagePrice = Data.average(cars, carMeas); 

　　　  System.out.println("平均价格为: "+ averagePrice);　　  
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解在第02~05行，声明了如下一个测量器的接口Measurer，在这个接口里，声明了一个measure( )方法，很明显，这是一个抽象方法，只有方法声明，而没有实现方法体。

此外，还应该注意到，在这个measure方法内，测量的是某个对象（Object），这个对象到目前为止，并不明确。

不明确的用意在于，先不绑定任何特定的对象。

第06~14行，通过AreaMeasurer类来实现（implement）Measurer接口。

这时，把抽象的方法measure( )具体化，把抽象的对象明确化（Rectangle aRectangle = (Rectangle) anObject），才能使用。

需要注意的是，在Java的继承体系中，由于Object对象是所有对象的“鼻祖”，因此，Object对象可以“化身”为任何类型对象的引用。

第42~58行，定义了一个Data类，这个类负责求某个对象属性的均值。

但需要注意的是，这个方法average( )所代表的算法，和其操作的对象是松耦合的。

因为这个average( )方法的第一个参数是抽象的对象（Object）类型数组，第二个参数是抽象的测量接口Measurer类型。

其特别之处在于，把求均值这个方法和求均值的对象暂时分割开（也可以认为是解耦）。

随后，当我们遇到对象是矩形，那么我们就求矩形面积的均值（第06~14行）。

如果后期我们遇到对象是汽车，那么我们就求这些汽车售价的均值（第15~41行）。

显然，这种延后确定对象，之后“有的放矢”地求均值机制，让这个方法更具有一般性和通用性。

虽然求均值的方法是一样的：各对象值求和/对象个数。

但不同的对象，有不同的测量方法，而这些不同的个性化测算方法，则是来自于对接口Measurer的不同实现版本，即不同的对象，实现不同版本的measure( )方法。

第06~14行显示的是矩形的测算方法，而第33~41行则显示的求汽车价格的测算方法。

【范例分析】上面代码中第63行，明确测量的对象为面积测量，第64~69行定义一些列的矩形对象。

然后调用Data类的静态方法average( )，实参rects（矩形对象数组）给这个方法中的第一个参数——形参objects赋值，第二个参数的实参areaMeas，实际上是一个面积测量的对象，被赋值给形参meas。

前面涉及几个类和接口之间的UML关系，如下图所示。

类似的，第73行，明确测量的对象为计算汽车销售价格均值，第74~79行定义一些列的矩形对象（即对象数组）。

然后调用average( )方法，实参cars（汽车对象数组），给这个方法中的第一个参数——形参objects赋值，第二个参数的实参carMeas，实际上是一个价格计算的对象，被赋值给形参meas。

由上分析可知，Data类中的average( )方法，从Rectangle、Car等类中解耦出来。

Rectangle类和Car类，也不再和其他类耦合，取而代之的是，我们提供了一个诸如AreaMeasure、CarMeasure等小助手（即接口Measurer的一个具体实现）。

这个助手类存在的唯一目的，就是告诉average方法，如何来测量对象的某种属性值的平均值。

我们知道，控制反转关注的是，一个对象如何获取他所依赖的对象的引用，这是责任的反转。

请读者参照范例9-8，分析一下，在范例9-9中，控制反转（或者是角色注入）体现在什么地方呢？
<a id="3"></a>
## 9.3 内部类

所谓的内部类，就是指在一个类的内部又定义了其他类。

如果在类Outer的内部再定义一个类Inner，此时类Inner就称为内部类，而类Outer则称为外部类。

内部类可声明为public或private。

当内部类声明为public或private时，对其访问的限制与成员变量和成员方法完全相同。


### 9.3内部类的名称不需要和.java文件相同。

9.3.1 内部类的基本定义内部类的定义格式如下所示。

标识符 class 外部类的名称{　 // 外部类的成员　 标识符 class 内部类的名称 　 {　　  // 内部类的成员 　 }}内部类主要有如下作用。

（1）内部类提供了更好的封装，可以把内部类隐藏在外部类之内，不允许同一个包中的其他类访问该类。

（2）内部类成员可以直接访问外部类的私有数据，因为内部类被当成其外部类成员，同一个类的成员之间可以相互访问。

但外部类不能访问内部类的实现细节，例如，内部类的成员变量。

（3）匿名内部类适合用于创建那些仅需要一次的类。

范例9-10 内部类的使用（ObjectInnerDemo.java）
```java
　class Outer 
　{
　　 int score = 
;
　　 void inst() 
　　 {
　　　  Inner in = new Inner();
　　　  in.display();　　 
　　 }
　　 public class Inner 
　　 {
　　 // 在内部类中声明一个name属性
　　　  String name = "张三";
　　　  void display() 
　　　  {　　　　
　　　　　System.out.println("成绩: score = " + score);//输出外部类中的属性
　　　  }
　　 } 
　}
　public class ObjectInnerDemo 
　{
　　 public static void main(String[] args)
　　 {
　　　  Outer outer = new Outer();
　　　  outer.inst();
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解第04~08行声明了一个inst()方法，用于实例化内部类的对象in。

第09~17行，在Outer类的内部声明了一个Inner类，此类中有一个display()方法，用于打印外部类中的score属性。

【范例分析】从程序中可以看到，内部类Inner可以直接调用外部类Outer中的score属性，现在如果把内部类拿到外面来单独声明，那么在使用外部类Outer中的score属性时，则需要先产生Outer类的对象，再由对象通过点操作（“.”），调用Outer类中的公有接口（也就是公有方法），然后再由这些公有接口“间接”地访问score属性。

由此可以看到，由于使用了内部类操作，程序在访问score属性的时候，减少了创建对象的操作，从而省去了一部分的内存开销。

需要读者注意的是，内部类是一个编译时的概念，一旦编译成功，事实上，就会生成完全不同的两个类（类个数总和取决于内部类的个数加上外部类个数）。

对于一个名为Outer的外部类和名为Inner的内部类，编译完成后出现Outer.class和Outer$Inner.class两个类，以及包含主方法的测试类ObjectInnerDemo，如上图所示，其中Outer$Inner.class就是一个编译好的内部类，而“$”就表示隶属关系。

在运行时需要注意的是，只能用java 来解析含有主方法的类ObjectInnerDemo。

9.3.2 在方法中定义内部类内部类不仅可以在类中定义，也可以定义在方法体或作用域内（即由“｛｝”括起来的区域）。

这样的内部类作用范围仅局限于方法体或特定的作用域内，因此也称为局部内部类。

下面举例说明。

范例9-11 在方法中定义内部类（ObjectInnerClass.java）
```java
　class InnerClassTest
　{
　　 int score = 
;
　　 void inst( )
　　 {
　　　  class Inner
　　　  {
　　　　　void display( )
　　　　　{
　　　　　　 System.out.println("成绩: score = " + score);
　　　　　}
　　　  }
　　　  Inner in = new Inner( );
　　　  in.display( );
　　 }
　}
　public class ObjectInnerClass
　{
　　 public static void main(String[] args)
　　 {
　　　  InnerClassTest outer = new InnerClassTest();
　　　  outer.inst( );
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解在InnerClassTest类中的第04~15行声明了一个inst( )方法，在此方法中又声明了一个名叫Inner的内部类，同时产生了Inner的内部类实例化对象（第13行），调用其内部的方法display( )（第14行）。

第21行产生了一个InnerClassTest类的实例化对象outer，并在第22行调用Outer类中的inst( )方法。

【范例分析】在命令行下运行Java程序，可以显示更多细节，如下图所示。

像上一个类一样，编译完成后出现多个类，而且只能用java来解析含有主方法的类ObjectInnerClass。

像其他类一样，局部内部类也可以进行编译，所不同的是，作用域不同而已，局部内部类只在该方法或条件的作用域内才能使用，出了这些作用域后，便无法引用。

读者可以把局部内部类想象成一个普通的数据类型，普通的数据类型在某个方法体内或作用域内，定义了一个局部变量，出了它所定义的作用域范围，它的生命周期就到头了，其他地方自然也就无法引用它。

<a id="4"></a>
## 9.4 匿名内部类

有时候，我们懒得去给内部类命名，这时就倾向于使用匿名内部类。

因为匿名内部类没有名字，所以它的创建方式也比较特别。

创建格式如下所示。

new 父类构造器（参数列表）|实现接口(){ //匿名内部类的类体部分 }这里，我们可以看到，使用匿名内部类，我们必须要继承一个父类或实现一个接口。

需要注意：①匿名内部类是没有class关键字做修饰的；② 匿名内部类是直接使用new来生成一个对象的引用。

在new之前，这个匿名内部类是要先定义的。

范例9-12 匿名内部类使用实例（AnonymousInnerClass.java）
```java
　abstract class Bird
　{
　　 private String name;
　　 public String getName()
　　 {
　　　  return name;
　　 }
　　 public void setName(String name)
　　 {
　　　  this.name = name;
　　 }
　　 public abstract int fly();
　}
　
　public class AnonymousInnerClass 
　{
　　 public void birdBehaviour(Bird bird)
　　 {
　　　  System.out.println(bird.getName() + “最高能飞 " + bird.fly() + "米");
　　 }
　　 public static void main(String[] args)
　　 {
　　　  AnonymousInnerClass AnonyObjObj = new AnonymousInnerClass();
　　　  AnonyObjObj.birdBehaviour(new Bird()
　　　　　{
　　　　　　 public int fly()
　　　　　　 {
　　　　　　　  return 1000;
　　　　　　 }
　　　　　　 public String getName()
　　　　　　 {
　　　　　　　  return "小鸟";
　　　　　　 }
　　　　　});
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解代码第01~13行，定义了一个抽象类Bird，里面有个仅有方法声明而无方法体的抽象方法——fly( )。

根据前面学习到的知识，我们知道，如果抽象类Bird内部的抽象方法没有具体化，永远都是抽象类，没有办法用new关键字，创建一个实例。

第17行，在birdBehaviour方法的参数列表中，bird仅仅作为方法体的形参——也就是形式上的参数，换句话说，它天生就是来接纳实参（实际上的参数）来赋值的，所以参数列表中并不涉及生成新对象。

在第23行，生产一个AnonymousInnerClass类的对象AnonyObjObj。

接着，重点来了，在第24行，对象AnonyObjObj使用自己类的公有方法birdBehaviour( )，此刻，这个方法的参数要做实了，它需要一个实实在在的Bird对象。

而我们知道，Bird本身还是一个抽象类，想定义对象，必须先把这个类中的抽象方法变得不抽象（也就是设计实现部分）。

假设这个抽象类的非抽象化仅仅就用一次，那么这个类定义出来的实例对象叫什么名字也无所谓，索性就不给它取名字，用一个匿名类好了。

于是，在第25~35行，实际上，就重新定义了抽象类，主要目的还是让抽象方法fly( )不再抽象了。

然后，第24行用new 操作，创建了一个无名小鸟bird，当作实参，传递给birdBehaviour( )。

由此可以看到，第24~35行代码的目的就是要生产出来一个“一次性”的、用完就扔的Bird类实例而已。

但因为这种“偷懒”的方法，让代码的可读性变得较差，所以并不推荐。

请读者思考，在这个范例中，如何改成可读性较好的非匿名类实现同样的功能？提示匿名内部类存在一个缺陷，就是它仅能被使用一次，创建匿名内部类时，它会立即创建一个该类的实例，该类的定义会立即消失，所以匿名内部类不能够被重复使用。
<a id="5"></a>
## 9.5 匿名对象

匿名对象，顾名思义，就是没有明确的声明的对象。

读者也可以简单地理解为只使用一次的对象，即没有任何一个具体的对象名称引用它。

请看下面的范例。

范例9-13 匿名对象的使用（AnonymousObject.java）
```java
　class Person
　{
　　 private String name = "张三";
　　 private int age = 
;
　　 public String talk( )
　　 {
　　　  return "我是：" + name + "，今年：" + age + "岁";
　　 }
　}
　public class AnonymousObject 
　{
　　public static void main(String[] args)
　　 {
　　　  System.out.println(new Person( ).talk( ));
　　 }
　}
```
保存并运行程序，结果如下图所示。

代码详解第01~09行声明了一个Person类，里面有name和age两个私有属性，并分别赋了初值。

第14行声明了一个Person匿名对象，通过“new Person( )”产生一个匿名对象，然后再通过“对象.方法名”的Java语法格式，调用Person类中的talk( )方法。

【范例分析】从程序中可以看到，用“new Person( )”声明的对象，它并没有赋给任何一个Person类对象的引用，所以此对象只使用了一次，用完之后，就会被Java的垃圾收集器回收。

现在总结一下匿名对象的特点。

（1）匿名对象不会被其他对象所引用。

（2）匿名对象是“一次性（disposable）”的对象产品，使用一次就变成垃圾了，被垃圾回收器收回了。

有意思的是，英文单词中的“disposable”，有“可任意处理的”和“用完即可丢弃的”这两层含义，都可以用于形容“匿名对象”。

<a id="6"></a>
## 9.6 高手点拨

1. 继承一个抽象类和继承一个普通类的主要区别（1）在普通类之中所有的方法都是有方法体的，如果说有一些方法希望由子类实现的时候，子类即使不实现，也不会出现错误。

而如果重写改写了父类的同名方法，就构成了“覆写”。

（2）如果使用抽象类的话，那么抽象类之中的抽象方法，在语法规则上就必须要求子类给予实现，这样就可以强制子类做一些固定操作。

2. 接口不能实例化对象我们可以声明一个接口对象的变量（引用），假设我们定义一个接口faceA 。

interface  faceA  // 定义一个接口A
{　　 
    void doSomething( );
}

下面的定义是合法的。

faceA myface;但是，我们不能用接口构造一个对象，如下代码是错误的。
```java
faceA myface = faceA( );// 错误原因很简单，接口不是一个类，接口中的方法基本上都是抽象的，所以不能用它构造（通过new操作）一个对象。
```

但一个接口变量（即引用）却可以指向它的子类对象（也就是通过“实现”这个接口的类的对象），如下所示。
```java
class  myClass implements faceA  // 定义一个接口A
{　　 
    @Override　 void doSomething( )　 
    {　　  
        Doing something;　
    }　 
    void doNewSomething( )　 
    {　　  
        Doing new thing;　 
    }
}
```
```java
faceA  myface = new myClass();  //正确，但只能访问myClass从接口faceA“实现”的方法
```
3. 接口、抽象类、类、对象的关系（1）基本类：也就是一般的类（一般所说的类就是基本类），是对象的模板，是属性和方法的集合。

可以继承其他的基本类（继承一个）、抽象类（继承一个）、实现接口（实现多个）。

（2）抽象类：有抽象方法的类(抽象方法就是该方法必须由继承来实现，本身只定义，不实现)。

抽象类可以有一个或多个抽象方法，它是基本类和接口类的过渡。

（3）接口：接口中的所有方法除默认方法（带方法体）外都是抽象方法，抽象方法本身只定义，不实现，用来制定标准。

四者间的关系如下图所示。

实际上，所谓的接口就是指在类的基础上的进一步抽象（抽离数据，保留行为）。

而很多时候在开发之中，也会避免抽象类的出现，因为抽象类毕竟存在单继承的局限。

类与类之间的共性就成了接口的定义标准。

类、抽象类、接口之间的角色扮演，可以用如下的例子来做类比。

比如说，在一个公司里，有老板、老板聘用的经理和员工3种角色。

普通类就好比是员工，抽象类就好比是经理，接口就好比是老板。

在接口里，“老板”就是动动嘴皮子，光提方法，但他自己不去实现。

比如，老板说我要那个文件，给我定个机票，我要那个策划方案等，都是手下的人去实现。

在抽象类中，它给出的方法，有的是他自己做，有的是其他人做（即继承于它这个类的子类）。

比如经理说我要那个文档，员工就要发给他，但是他自己也要做点事，比如拿方案给老板看。

一言蔽之，经理（抽象类）需要又说又做。

相比而言，普通类“脚踏实地”，自己给出的方法要非常具体，什么都要实现，亲力亲为。

4. 接口和抽象类的应用抽象类（abstract）在Java语言中体现了一种继承关系，要想使继承关系合理，父类和派生类之间必须存在“IS A”关系，即父类和派生类在概念本质上应该是相同的。

对于interface 来说则不然，并不要求interface的实现者和interface定义在概念本质上是一致的，仅仅是实现了interface定义的契约而已。

考虑这样一个例子，假设建立一个关于Door的抽象概念，一般认为Door可执行两个动作：open和close，若通过abstract class或interface来定义一个表示该抽象概念的类型，定义方式分别如下所示。

使用abstract 类方式定义Door。
```java
abstract class Door 
{  　 
    abstract void open();  　 
    abstract void close();  
}
```
使用interface方式定义Door。
```java
interface Door 
{  　 
    void open();  　 
    void close();  
}
```
其他具体子类，比如说子类——木门类（WoodDoor）或铁门类（IronDoor）等可以通过extends（扩展）继承抽象类Door中定义的两个方法open()和close()。

类似地，木门类或铁门类也可以通过关键字implements，同样继承使用接口Door中的两个方法。

这样看起来，使用abstract class和interface好像没有太大的区别。

事实上，并非如此。

比如说，如果用户的需求发生变化，现在要求所有的Door都要具备报警的功能，那该如何设计这个类结果呢？解决方案一简单地在抽象类Door中新增加一个alarm的方法如下所示。
```java
abstract class Door
{  　 
    abstract void open();  　 
    abstract void close();  　 
    abstract void alarm();  //新添加一个抽象方法
}
```
那么，具有报警功能的子类AlarmDoor继承上述变更的父类即可，具体代码如下所示。
```java
class AlarmDoor extends Door 
{  　 
    void open() { … }  //实现继承而来的方法open()　 
    void close() { … }  //实现继承而来的方法close ()　 
    void alarm() { … }  //实现继承而来的方法alarm ()
}
```
另外一种修改方式是利用interface实现，如下所示。
```java
interface Door 
{  　 
    void open();  　 
    void close();  　 
    void alarm();  //新添加一个报警接口alarm
}
```
那么，具有报警功能的子类AlarmDoor通过implements继承接口添加新方法，具体代码如下所示。

```java
class AlarmDoor implements Door 
｛  　 
     void open() { … }  　 
     void close() { … }  　 
     void alarm() { … }  
｝
```
然而，直接在抽象类或接口中新增加alarm方法，其实是违反了面向对象设计中的一个核心原则——接口隔离原则（Interface Segregation Principle，ISP）。

前面的行为，即把Door概念本身固有的行为方法（如close和open）和另外一个概念“报警器”的行为方法混在了一起。

这样就会引起一个问题，那些仅仅依赖于Door这个概念的模块，会因为抽象类（父类）“添加报警器”这个方法的改变而被迫改变，并不是所有的子类都需要报警功能的。

在一个接口中添加一个新方法，也会导致所有使用这个接口的子类被迫使用这个它可能不需要的方法。

此外，这种不断地在接口中添加新方法的策略，也会使原来的Door接口变得越来越“胖”，这就是所谓的“接口污染”。

解决方案二事实上，我们还有第二种方法。

显然，open、close和alarm属于两个不同的概念，前两个（open、close）是必备功能，而alarm是附加功能。

根据ISP原则，应该把它们分别定义在代表这两类概念的两个抽象类中。

定义的可能方式有3种。

（1）这两个概念都使用abstract class方式定义。

点评：因为Java语言不支持多重继承，所以两个概念都使用abstractclass方式定义是不可行的，因为其子类不可能同时继承“Door”和“Alarm”两个类，从而达成AlarmDoor功能的汇集。

（2）两个概念都使用interface方式定义。

点评：在概念本质上，无法明确体现AlarmDoor，到底是Door，还是报警器，无法反映AlarmDoor在概念本质上和Door是一致的。

（3）一个概念使用abstract class方式定义，另一个概念使用interface方式定义。
```java
abstract class Door 
{  　 
    abstract void open();  　 
    abstract void close()；  
}  
interface Alarm 
{  　 
    void alarm();  
}  
class AlarmDoor extends Door implements Alarm 
{  　 
    void open() { … }  　 
    void close() { … }  　 
    void alarm() { … }  
}
```

点评：这是一个“中庸”的方案，比较符合我们的要求，在概念上继承了“Door”的所有特性，同时，又通过实现接口，在功能上完成了“扩展”。

抽象类在Java语言中表示一种继承关系，而继承关系在本质上是“is a”关系，对于Door这个概念，我们应该使用abstract class方式来定义。

interface表示的是“like a”关系，AlarmDoor又具有报警功能，说明它又能够完成报警概念中定义的行为。
<a id="7"></a>
## 9.7 实战练习

1.设计一个限制子类访问的抽象类实例，要求在控制台输出如下结果。

教师——&gt;姓名：刘三，年龄：50，职业：教师工人——&gt;姓名：赵四，年龄：30，职业：工人2.利用接口及抽象类设计实现。

（1）定义接口圆形CircleShape()，其中定义常量PI，默认方法area计算圆面积。

（2）定义圆形类Circle实现接口CircleShape，包含构造方法和求圆周长方法。

（3）定义圆柱继承Circle实现接口CircleShape，包含构造方法、圆柱表面积、体积。

（4）从控制台输入圆半径，输出圆面积及周长。

（5）从控制台输入圆柱底面半径及高，输出圆柱底面积、圆柱表面积及体积。

3.定义一个包含“name”“age”和“sex”的对象，使用匿名对象输出对象实例。

4.完成一个统计Book类产生实例化对象的个数。