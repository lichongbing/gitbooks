更强大和方便的功能——注解JDK 5.0以后增加了注解，注解不但增强了程序编写的方便性，而且程序员可以通过反射机制，完成对编程信息的访问。

本章介绍注解的用法、自定义注解、通过反射访问注解及通过注解生成注释等内容。

本章要点（已掌握的在方框中打钩）注解概述常用内置注解自定义注解通过反射访问注解11.1 注解概述注解（Annotation），或叫注释，是JDK 1.5以后引入的注释的语法，但是它却区别于普通的注释，普通的代码注释通过“//”或“/*….*/”即可完成注释。

注解除了具备简单的注释功能外，更多的可以完成“配置”式的编程。

通过注解可以配置一些编程的元数据，比如对类、方法、变量、属性等的声明，通过注解的声明可以在编译时、类加载时和运行时实现对这些声明的访问，从而完成更加灵活的程序设计。

实际上，注解是一种接口定义，通过该接口定义，再利用Java的反射机制来完成其信息的访问。

一般来讲，通过JDK内置的Annotation和自定义的Annotation主要可以完成以下几个功能。

控制JavaDoc文档的生成。

跟踪代码的依赖性，实现配置式编程。

运行时访问编程元数据。

编译时实现格式检查。

注解被广泛应用到各种开发环境中，目前流行的开发框架SSH（Struts、Spring、Hibernate）中就大量地使用了注解，比如在Spring的开发配置中，既可以通过编写XML配置文件来实现各种Bean的管理和注入，同时可以利用注解的方式，直接在编程时实现Bean的声明和注入，这些实际上就是利用注解和反射机制，访问了编程元数据来实现的。

本章接下来讲解一下JDK内置的一些常用注解用法，自定义注解方法和注解较为复杂的一些用法。

11.2 常用内置注解在JDK 5.0中，内置了一些注解，通过这些注解方便我们对程序的控制和编写，方便JavaDoc的输出控制。

内置注解分为两类，一类是元注解，另一类是普通注解。

所谓的元注解就是对注解的注解，这个我们在本章的自定义注解小节讲解，下面主要介绍普通注解。

常见的普通注解有@Override、@Deprecate、@SuppressWarnings等。

注解的特殊使用方法就是必须在关键字前面加上“@”，无论是内置注解还是自定义注解均是这样。

@Override注解用来告诉编译器，@Override声明的方法是覆盖超类方法的。

@Deprecate注解告诉编译器本方法不建议使用。

@SuppressWarnings注解用来抑制警告信息的显示。

@Documented注解则用来将自定义的注解设置成文档说明。

下面一一举例说明。

范例11-1 通过@Override覆盖超类方法

```java
 package chapter;
　public class ch11_1 {
　    　 public void test(){
　    　　 System.out.println("ok");
　    　 }
　}
　class subCh11_1 extends ch11_1{
　    　 @Override
　    　 public void Test(){
　    　　System.out.println("ok");
　    　 }
　 }
```
 代码详解第09行的本意是要覆盖超类ch11_1的方法test，但是名字Test的首字母写成了大写，这样就无法实现对超类方法的覆盖，因为覆盖必须方法名相同，返回值相同，参数也相同。

这时候可以加上第08行的@Override注解，该注解指明Test方法是对超类方法的覆盖，因此编译器会检查是否有覆盖错误。

本例编译通不过，只有把Test的首字母改成小写后，方可运行。

范例11-2 通过@SuppressWarnings关闭警告信息
```java
 package chapter11;
　public class ch11_2 {
　　 public static void main(String args[]){
　    　　 @SuppressWarnings("unused")
　    　　 int a;
　    　　 String bString="ok";
　    　　 System.out.println("@SuppressWarnings description");
　    　 }
　 }
```
 代码详解第05行和第06行分别定义了2个局部变量，编译时，第06行会报一个警告错误“The value of the local variable bString is not used”，意思是说本地变量bString虽然定义了却没有被使用，这个警告错误是不影响运行的，为了避免出现这种错误提示，可以像第04行一样，加入@SuppressWarnings("unused")注解，这样就可以避免警告错误的提示。

@SuppressWarnings可以标注在类、字段、方法、参数、构造方法，以及局部变量上，除了unused外，还可以用unchecked、serial、deprecation等忽略对应的警告信息。

范例11-3 通过@Deprecate告知编译器被标注的元素是不希望被使用的
```java
 package chapter11;
　public class ch11_3 {
　    　 public static void main(String[] args) {    
　    　　 ch11_3_1.test1();
　    　　 ch11_3_1.test2();
　    　 }
　}
　class ch11_3_1{
　    　 @Deprecated
　    　 public static void test1(){
　    　　 System.out.println("test1 method is deprecated");
　    　 }
　    　 public static void test2(){
　    　　 System.out.println("test1 method is pray");
　    　 }    
  }
```
 代码详解第09行加入@Deprecated注解后，第04行调用时，系统会弹出警告信息，告知test1方法已经不再使用了。

JDK为了兼容老版本的API，很多方法都加入了@Deprecated，使用这些老的方法时都会提示警告信息，但不影响运行。

11.3 自定义注解自定义注解允许开发者开发自己的注解，从而实现更加灵活和复杂的编程思想。

自定义注解的语法如下所示。

[public] @interface 自定义注解的名称{    [数据类型 变量名称();]}注意@interface的写法，必须加上“@”，另外就是注解的变量声明，每个变量后面加上“()”，定义注解时，一般还要指明注解的作用范围，通过@Retention注解来指明，也就是说@Retention 注解时定义注解的注解，我们称为元注解，常见的元注解有@Target、@Retention、@Documented、@Inherited。

因此在定义注解时，往往配合元注解来丰富和完善注解的定义。

@Retention表示在什么级别保存该注解信息。

可选的参数值在枚举类型 RetentionPolicy中，该枚举类型的值如下表所示。




|  枚举值 | 说明  |
| ------------ | ------------ |
| RetentionPolicy.SOURCE  |  注解将被编译器丢弃 |
| RetentionPolicy.CLASS  |  注解在class文件中可用，但会被JVM丢弃 |
| RetentionPolicy.RUNTIMEJVM  | 将在编译、加载、运行期均保留注解，因此可以通反射机制读取注解的信息｜

若没有指定@Retention，默认的编译器认为@Retention 指定的是RetentionPolicy.CLASS。

@Target 表示该注解用于什么地方，可能的值在枚举类 ElemenetType中，如下表所示。




|  枚举值 | 说明  |
| ------------ | ------------ |
|  ElemenetType.CONSTRUCTOR |  构造器声明 |
| ElemenetType.FIELD  | 域声明（包括 enum 实例）  |
| ElemenetType.LOCAL_VARIABLE  | 局部变量声明  |
| ElemenetType.ANNOTATION_TYPE  | 作用于注解量声明  |
|  ElemenetType.METHOD |  方法声明 |
| ElemenetType.PACKAGE  | 包声明  |
| ElemenetType.PARAMETER  |  参数声明 |
| ElemenetType.TYPE  | 类，接口（包括注解类型）或enum声明  |

@Documented 将此注解包含在 javadoc 中 ，它代表着此注解会被javadoc工具提取成文档。

在doc文档中的内容会因为此注解的信息内容不同而不同。

 @Inherited 允许子类继承父类中的注解。

范例11-4 自定义注解TestAnnoaction0
```java
 package chapter11;
　@interface testAnnoation0{
　    　 public String name() default "methodname";
　    　 public String unit() default "unit";
　}
　public class ch11_4 {
　    　 public static void main(String[] args) {
　    　 }
　    　 @testAnnoation0(name = "电池SOC", unit = "%")
　    　 public void testAnnoation(){        
　    　 }
　}
```
 代码详解第02~05行自定义了一个注解testAnnoation0。

第03行指定了注解的属性name，默认值为字符串“methodname”。

第04行指定了注解的属性unit，默认值为字符串“unit”。

第09行使用了该注解，并将注解的name属性设置为“电池SOC”，unit的值为 “%”。

范例11-5 自定义注解TestAnnoation1，指定注解的作用对象
```java
 package chapter11;
　import java.lang.annotation.ElementType;
　import java.lang.annotation.Target;
　@Target(ElementType.METHOD)
　@interface testAnnoation1{
　    　 public String name() default "methodname";
　    　 public String unit() default "unit";
　}
　public class ch11_5 {
　　 public static void main(String[] args) {
　    　 }
　    　 @testAnnoation1(name = "电池SOC", unit = "%")
　    　 public void testAnnoation(){        
　    　 }
　}
```
 代码详解第05行指定了注解testAnnoation用于方法的声明。

如果用在非方法的元素上，比如成员属性，那么编译是通不过的。

范例11-6 自定义注解TestAnnoation2，并指定什么级别保存该注解信息
```java
 package chapter11;
　import java.lang.annotation.ElementType;
　import java.lang.annotation.Retention;
　import java.lang.annotation.RetentionPolicy;
　import java.lang.annotation.Target;
　@Retention(RetentionPolicy.RUNTIME)
　@Target(ElementType.METHOD)
　@interface testAnnoation2{
　    　 public String name() default "methodname";
　    　 public String unit() default "unit";
　}
　public class ch11_6 {
　    　 public static void main(String[] args) {
　    　 }
　    　 @testAnnoation2(name = "电池SOC", unit = "%")
　    　 public void testAnnoation(){        
　    　 }
　}
```
 代码详解第06行指定了注解testAnnoation的保留级别为RetentionPolicy.RUNTIME，这就意味着该注解在编译、加载、运行期均保留注解信息。

范例11-7 通过@Document控制JavaDoc的输出
```java
 package chapter11;
　import java.lang.annotation.Documented;
　import java.lang.annotation.ElementType;
　import java.lang.annotation.Retention;
　import java.lang.annotation.RetentionPolicy;
　import java.lang.annotation.Target;
　@Documented
　@Retention(RetentionPolicy.RUNTIME)
　@Target(ElementType.METHOD)
　@interface testAnnoation{
　    　 public String name() default "methodnam"”;
　    　 public String unit() default "unit";
　}
　public class ch11_7 {
　    　 public static void main(String[] args) {
　    　 }
　    　 @testAnnoation(name = "电池SOC", unit = "%")
　    　 public void testAnnoation(){        
　    　 }
　}
```
 代码详解从第07~13行自定义了一个注解testAnnoation（关于如何自定义注解将在下一小节讲解），在第18行使用了该注解，注意如果在第07行不写@Documented注解，那么生成JavaDoc文档时，关于类ch11_4 中testAnnoation方法的说明如下。

细心的读者会发现，没有关于注解@testAnnoation的任何信息，但是当我们加上第07行的@Documented注解后，再生成的JavaDoc文档如下。

@testAnnoation注解信息显示出来了，也就是说@Documented在定义注解的时候，控制了是否在生成文档的时候生成有关注解的信息。

11.4 通过反射访问注解信息利用Java的反射机制，可以访问注解的信息。

比如在调用某个方法时，我们需要知道该方法的一些基本信息，而这些信息又需要动态获取时，利用反射获取注解信息是一个比较理想的处理方式，当然，我们直接了解某个类的某个方法的功能，了解返回数据的类型是较为常规的做法，但这种做法的前提是要先了解再调用。

反射首先要获取该类的类型信息，然后通过该类型信息就可以完成对注解信息的访问。

假设实例化的类名为ch8，获取类型信息如下。

Class class1=ch8.getClass();class1的getAnnotation方法和getAnnotations方法可以直接访问ch8类上的注解信息。

getAnnotation获取指定注解信息，getAnnotations获取所有注解信息。

通过Class1的getField方法访问ch8的成员属性，根据返回的Field类型的对象的getAnnotation方法和getAnnotations方法访问成员属性的注解信息。

通过Class1的getMethod方法访问ch8的成员方法，根据返回的Method类型的对象的getAnnotation方法和getAnnotations方法访问成员属性的注解信息。

范例11-8 访问类的某个成员方法的注解信息
```java
 package chapter11;
　import java.lang.annotation.Annotation;
　import java.lang.annotation.Documented;
　import java.lang.annotation.ElementType;
　import java.lang.annotation.Retention;
　import java.lang.annotation.RetentionPolicy;
　import java.lang.annotation.Target;
　import java.lang.reflect.Method;
　@Documented
　@Retention(RetentionPolicy.RUNTIME)
　@Target(ElementType.METHOD)
　@interface testAnnoation8{
　    　 public String name() default "methodname";
　    　 public String unit() default "unit";
　}
　public class ch11_8 {
　    　 public String aString;
　    　 public static void main(String[] args) {
　    　　 try {
　    　　　  ch11_8 ch8=new ch11_8();
　    　　　  Method method=ch8.getClass().getMethod("getData1");            
　    　　　  Annotation ans[]=method.getAnnotations();
　    　　　  for (Annotation annotation : ans) {
　    　　　　　 System.out.println(annotation);
　    　　　  }
　    　　　  Annotation annotation=method.getAnnotation(testAnnoation8.class);
　    　　　  System.out.println(annotation);
　    　　 } catch (Exception e) {
　    　　　　e.printStackTrace();
　    　　 }
　    　 }
　    　 @Deprecated
　    　 @testAnnoation8(name = "电池SOC", unit = "%")
　    　 public void getData1(){        
　    　 }    
　}
```
 代码详解从第09~15行自定义了一个注解testAnnoation。

第16~36行定义了类ch11_8。

第32~35行定义方法getData1，方法上有两个注解@Deprecated和@testAnnoation8(name = "电池SOC", unit = "%")。

第20行定义了ch11_8的对象ch8。

第21行访问ch8的成员方法getData1。

第22~25行访问getData1方法上的所有注解。

第26~27行访问了指定注解testAnnoation8，注意指定注解传递的参数是testAnnoation8.class，也就是类的类型信息对象。

范例11-8的输出结果如下所示。

@java.lang.Deprecated()@chapter11.testAnnoation8(unit=%, name=电池SOC)@chapter11.testAnnoation8(unit=%, name=电池SOC)范例11-9 访问类的某个成员方法的注解信息
```java
 package chapter11;
　import java.lang.annotation.Annotation;
　import java.lang.annotation.Documented;
　import java.lang.annotation.ElementType;
　import java.lang.annotation.Retention;
　import java.lang.annotation.RetentionPolicy;
　import java.lang.annotation.Target;
　import java.lang.reflect.Method;
　@Documented
　@Retention(RetentionPolicy.RUNTIME)
　@Target(ElementType.METHOD)
　@interface testAnnoation9{
　    　 public String name() default "methodname";
　    　 public String unit() default "unit";
　}
　public class ch11_9 {
　    　 public String aString;
　    　 public static void main(String[] args) {
　    　　 try {
　    　　　 ch11_9 ch9=new ch11_9();
　    　　　 Method method=ch9.getClass().getMethod("getData1");            
　    　　　 Annotation annotation=method.getAnnotation(testAnnoation9.class);
　    　　　 testAnnoation9 t9=(testAnnoation9)annotation;
　    　　　 System.out.println("name value is "+t9.name()+"; unit is "+t9.unit());
　    　　 } catch (Exception e) {
　    　　　　e.printStackTrace();
　    　　 }
　    　 }
　    　 @Deprecated
　    　 @testAnnoation9(name = "电池SOC", unit = "%")
　    　 public void getData1(){        
　    　 }    
　}
```
 代码详解第23行将注解强制转换为testAnnoation9。

第24行访问了testAnnoation9注解的name属性和unit属性，并打印其值。

输出结果如下所示。

name value is 电池SOC; unit is %11.5 高手点拨当调用大量方法，且每个方法返回值和类型较多时，可以使用反射和注解简化编程。

我们对范例11-9进行改造，假设范例11-9的getData方法有很多，而且每个方法参数的个数和返回值都不同，如范例11-10所示。

范例11-10 访问类的某个成员方法的注解信息
```java
 package chapter11;
　import java.lang.annotation.Annotation;
　import java.lang.annotation.Documented;
　import java.lang.annotation.ElementType;
　import java.lang.annotation.Retention;
　import java.lang.annotation.RetentionPolicy;
　import java.lang.annotation.Target;
　import java.lang.reflect.Method;
　import java.util.ArrayList;
　
　@Documented
　@Retention(RetentionPolicy.RUNTIME)
　@Target(ElementType.METHOD)
　@interface testAnnoation10{
　    　 public String name() default "methodname";
　    　 public String unit() default "unit";
　}
　public class ch11_10 {
　      public static void main(String[] args) throws Exception{
　    　　ch11_10 ch9=new ch11_10();
　    　　Method method[]=ch9.getClass().getMethods();
　    　　for (Method method2 : method) {
　    　　　 Annotation annotation=method2.getAnnotation(testAnnoation10.class);
　    　　　 Class<?>; ts[]=method2.getParameterTypes();
　    　　　 if (method2.getName().indexOf("getData")==-1) continue;
　    　　　 ArrayList<Object>; params=new ArrayList<Object>;();
　    　　　 for (Class<?>; class1 : ts) {
　    　　　　　if (class1.getSimpleName().equals("int")){
　           params.add(10);
　    　　　　　}
　    　　　　　if (class1.getSimpleName().equals("String")){
　          params.add("100");
　    　　　　　}                    
　    　　　 }
　    　　　 if (annotation!=null){
　    　　　　　testAnnoation10 t9=(testAnnoation10)annotation;        
　　 System.out.println(t9.name()+" is "+method2.invoke(ch9, params.toArray())+" "+t9.unit());
　    　　　  }            
　    　　 }            
　      }
　      @testAnnoation10(name = "SOC", unit = "%")
　      public int getData1(int a){
　    　　return a;
　      }
　      @testAnnoation10(name = "Electricity", unit = "Ah")
　      public String getData2(String b){
　    　　return b;
　      }
　      @testAnnoation10(name = "Tempreture", unit = "℃")
　      public int getData3(int a,int b){
　    　　return a+b;
　      }
　}
```
 代码详解第11~17行定义了注解testAnnoation10。


第41~42行使用了注解testAnnoation10，并分别给每个注解的属性赋予了不同值，getData1是“SOC”，getData2是“Electricity”，getData3是“Tempreture”。


第21行获取ch9上的所有方法。


第23行获取每个方法上的testAnnoation10注解信息。


第24行获取每个方法的参数类型。


第27~32行给每个方法的参数赋值。


第37行利用注解信息，打印每个方法（getData1、getData2、getData3）执行的结果，注解中的name和unit是不同的。


输出结果如下所示。


SOC is 10 %Electricity is 100 AhTempreture is 20 ℃11.6 实战练习参照范例11-10，修改注解，使得调用者可以利用注解对方法进行分类，打印每个分类信息和每个分类下的方法及方法执行的结果。


（提示：给注解加上category属性，在使用注解的时候给每个category赋予类别值即可）。


