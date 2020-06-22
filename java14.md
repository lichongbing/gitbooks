##更灵活的设计——泛型
JDK 5.0以后增加了泛型，泛型可以通过一种类型或方法操作各种不同的类型，其提供了编译时类型的安全性。
这是一个比较大的改动，甚至有些Java的API都进行了重写，泛型的引入方便了我们的开发。
通过本章的学习，读者将理解并掌握泛型的概念和使用方法，包括泛型类和泛型方法。
本章要点（已掌握的在方框中打钩）泛型概念泛型类、泛型方法和泛型接口泛型使用的限制泛型通配符泛型继承10.1 泛型的概念所谓泛型，就是允许在定义类、接口的时候指定类型形参（类型的形式参数的简称），这个类型形参将在声明变量、创建对象时确定，即传入实际的类型参数，也可称为类型实参，这实际上是将数据类型参数化。
泛型可以用来定义泛型类、泛型方法和泛型接口。
在JDK 5.0之后的代码中，如果定义了泛型，但是没有使用泛型的话，为了兼容之前版本的JDK，会给出一个警告错误，但不影响编译和运行。
范例10-1 JDK版本中有关泛型向下兼容的警告错误
```java
　public class Base <T>; {
　　 T m;
　　 Base(T t) {
　　　  m = t;
　　 }
　
　　 public void print() {
　　　  System.out.println("base print ：" + m);
　　 }
　}
```
　Base<String>; base=new Base<String>;
　Base<String>; base1=new Base("aa");第
行不会报警告错误，第
行会报“Base is a raw type”的错误。

.2 泛型类的定义泛型类的定义语法如下所示。
[访问修饰符] class 类名称&amp;lt;T&amp;gt;泛型类的定义主要作用在于在类被实例化后，方便传入具体的参数对类的成员属性和成员方法进行 替换。
范例10-2 泛型类定义
```java
　　 T m;
　　 Base(T t) {
　　　  m = t;
　　 }
　　 public T getM(){
　　　  return m;
　　 }
　　 public void print() {
　　　  System.out.println("base print ：" + m);
　　 }
　　 public static void main(String[] args) {
　　　  Base<String>; base=new Base<String>;("base class is general");
　　　  System.out.println(base.getM());
　　 }
　}
```
第01行定义了泛型类Base，并通过T来定义成员变量m，定义了getM方法的返回值和构造方法的参数t，13行实例了一个对象base，并传入String类作为T的类型，这个被称为泛型类的实例化，有点类似于类的实例化。
之后m、t的类型就变成了String，getM的返回值也是String。
其实，是把T作为参数来定义这几个变量的类型和方法的参数类型。
T可以用任何一种引用类型，但是不允许使用基本类型，如int、double、char、boolean等是不允许的。
类型类被定义后，可以使用T来定义其成员变量和成员方法的返回值与参数。
10.3 泛型方法的定义泛型方法主要用于容器类，Java中任何方法，包括静态的（注意，和泛型类不一样，泛型类不允许在静态环境中使用）和非静态的，均可以用泛型来定义，而且和所在类是否是泛型没有关系，下面是泛型方法的定义。
[public] [static] <T>; 返回值类型 方法名（T参数列表）范例10-3 泛型方法定义
```java
　public class GeneralMethod {　　
　　　  public static <U>; void print(U[] list) {
　　　　　System.out.println();
　　　　　for (int i = 0; i <; list.length; i++) {
　　　　　　 System.out.print(" " + list[i]);
　　　　　}
　　　　　System.out.println();
　　　  }
　　　  public static void main(String[] args) {
　　　　　String a[]={"a","b","c","d","e"};
　　　　　Character b[]={'1','2','3','4','5'};
　　　　　GeneralMethod.print(a);
　　　　　GeneralMethod.print(b);
　　　  }
　}
```
输出结果如下所示。
a b c d e1 2 3 4 5使用泛型方法时，至少返回值或参数有一个是泛型定义的，而且应该保持一致，否则可能会受到各种限制，因此，这里建议保持一致。
10.4 泛型接口的定义接口也可以定义为泛型的，语法如下所示。
[public] interface  <T>;范例10-4 泛型接口定义
```java
　public class GeneralInterface {
　　 public static void main(String[] args) {
　　　　System.out.println(new TestIBase().getA());
　　 }
　}
　interface IBase<T>;{　
　　public T getA();
　  public T getB();
　}
　class TestIBase implements IBase<String>;{　
　　public String getA() {　　
　　　　return "A";
　　}
　　public String getB() {　
　　　　return "B";
　　　 }　
　}
```
按照泛型接口的语法规定，不能在接口中使用泛型来定义成员属性，下面的定义方法是不被允许的，这一点和泛型类是不同的。
```java
　interface IBase<T>;{　
　　 T m;
　　 public T getA();
　　 public T getB();
　}
```
第02行会报“Cannot make a static reference to the non-static typeT”错误，这表示在接口中直接定义泛型成员属性是不被允许的。
10.5 泛型的使用限制和通配符的使用在泛型的使用过程中，有些情况是不能使用泛型的，有时开发者对泛型实例化也想进行一些限制，这些都可以通过泛型的使用限制来完成，尽管它们是有限的。
另外，在泛型的定义过程中，还可以使用通配符来提高泛型定义的灵活性。
10.5.1 泛型的使用限制这里泛型的使用限制有两种含义：其一是什么情况下不能使用泛型，其二是开发者想限制泛型的实例化过程。
以下几种情况泛型是不被允许的。
（1）不能使用泛型的形参创建对象。
下面的语句是错误的。
T o=new T();（2）不能在静态环境中使用泛型类的类型参数，下面的用法是错误的。
public class A<T>;{　 public static T t;//错误　 public T getA（）{//允许　  …　 }}（3）异常类不能是泛型的，换句话说，泛型类不能继承java.lang.Throwable类。
如类D的定义public class D <T>; extends java.lang.Throwable就是不被允许的。
（4）泛型不能初始化一个数组，但是可以声明数组。
下面的用法是错误的。
T [ ] b=new T[10];如果开发者想限制泛型的实例化，则可以通过下面的方法。
泛型类名<;T  extends  超类>;范例10-5 泛型类的实例化限制
```java
　public class Base<T extends supA>; {
　　　T m;
　　　Base(T t) {
　　　　　  m = t;
　　　}
　　　public T getM(){
　　　　  return m;
　　　}
　　 public void print() {
　　　　　 System.out.println("base print ：" + m);
　　　}
　　　public static void main(String[] args) {
　　　　　 B bb=new B("test B");
　　　　　 Base<;B>; base=new Base<;B>;(bb);//允许
　　　　　 Base<String>; base=new Base<String>;("base class is general");  //不允许
　　　　　 System.out.println(base.getM());
　　　}
　}
　class supA{
　　　public String toString(){
　　　　　 return "supA";
　　　}
　}
　class B extends supA{
　　　String b;
　　　public B(String b){
　　　　　 this.b=b;
　　　}
　　　public String toString(){
　　　　　 return "subB";
　　　}
　}
```
通过T extends supA将泛型实例化的对象限制到必须是supA的子类，所以第14行是允许的，而第15行是不允许的。
supA可以是接口，但是extends不能换成implements，必须使用extends。
10.5.2 通配符的使用引入通配符可以在泛型实例化时更加灵活地控制，也可以用在方法中控制方法的参数。
语法如下所示。
泛型类名<;?  extends  T>;或泛型类名<;?  super  T>;extends规定了“？”的上限，super规定了“？”的下限，还有一种做法是省略了extends，看起来是下面的形式。
泛型类名<;? >;这表示泛型实例化对象可以是任何允许的类型。
范例10-6 通配符在泛型类创建泛型对象中使用
```java
　class gent <T>;{　
　}
　public class testa {　
　　　public static void main(String[] args) {
　　　　  gent <;? extends String>; o;
　　　　  o=new gent<String>;();//正确
　　　　  o=new gent<;Number>;();//错误
　　　}　
　}
```
第4行的o对象声明中“? extends String”决定了泛型的实例化对象只能是String类或它的子类，所以第
行正确，而第07行是错误的。
范例10-7 通配符在方法参数中的使用
```java
　class supC{
　　　public String toString(){
　　　　　 return "supA";
　　　}
　}
　class Bc extends supC{
　　　String b;
　　public Bc(String b){
　　　　　 this.b=b;
　　　}
　　　public String toString(){
　　　　　 return "subB";
　　　}
　　　public void test(gent<;? extends supC>; o){　　
　　}
　　　public static void main(String[] args) {
　　　　　 Bc bc=new Bc("test");
　　　　　 gent<;Bc>; oGent=new gent<;Bc>;();
　　　　　 bc.test(oGent);　　
　　　}
　}
```
第14行定义了方法test的参数o，指明泛型参数必须是supC类或其子类，第19行是调用，oGent是supC的子类对象。
10.6 泛型的继承和实现泛型类和泛型接口被定义后，是可以被继承和实现的。
下面举例说明泛型类的继承和泛型接口的实现过程。
范例10-8 泛型类的继承
```java
　public class A<;E>;{
　　　E t;
　}
　public class B<;T,T1>; extends A<T>;{
　　　
　}
```
子类B在定义的时候，如果省略了A后的<T>;，那么B的T自动变成Object，建议定义时加上<T>;以保留父类的类型参数。
B类还可以增加新的泛型T1。
范例10-9 泛型接口的实现
```java
　interface IT<T>;{
　　　public T dis();
　}
　public class testIT<;E>; implements IT<;E>;{
　　　E e;
　　　public testIT(E e){
　　　　　 this.e=e;
　　　}
　　　public E dis() {　　
　　　　　 return e;
　　　}
　　　public static void main(String[] args){
　　　　　 testIT<String>; tt=new testIT<String>;("test");
　　　　　 System.out.println(tt.dis());
　　　}
　}
```
实现类testIT不能省略<;E>;，必须和普通实现类一样，实现IT接口中的所有方法。
10.7 高手点拨1.泛型的使用大大增加了程序设计的灵活性，必要时，方法的名字可以用泛型替代，如下所示。
```java
　public class SupGent {
　　 public class A<;E>;{
　　　　 E t;
　　　　 public A(E t){
　　　　　　  this.t=t;
　　　　 }
　　　　 public E E(){
　　return t;
　　　　 }
　　 }
　　 public class B<;E>; extends A<;E>;{
　　　　 public B(E t){
　　super(t);
　　　　 }
　　　}
　　　public static void main(String[] args){　
　　　　　SupGent.B<String>; b=(new SupGent()).new B<String>;("test");
　　　　　System.out.println(b.E()); 　
　　　}
　}
```
第07行采用了泛型E，碰巧方法的名字也是E，只不过不要弄混，上例输出结果为test。
2.在进行数据库DAO封装操作时，采用泛型可以简化开发。
```java
　public class BaseDAO <T>;{
　　 public void Save(T t){　}
　　 public void Del(T t){　}
　　 public void Update(T t){　}
　　 public void Search(T t){　}
　}
　class TeacherDao extends BaseDAO<;Teacher>;{
　　 public void Save(Teacher t){　}
　　 public void newOperator(Teacher t){　}
　}
　class StudentDao extends BaseDAO<;Student>;{
　　 public void Save(Student t){　}
　　 public void newOperator2(Student t){　}
　}
```
　class Teacher{}
　class Student{}BaseDAO定义了基本的数据库增删改查，之后可以继承该泛型类，实现各自的增删改查，或者使用超类的增删改查，同时每个继承类还可以增加自己的操作。
10.8 实战练习参照高手点拨中的第2题，完善例子中的代码，实现教师或学生的增删改查，尝试给TeacherDao、StudentDao增加新的数据库操作。
