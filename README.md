# 1 索引介绍
> <font color='red'>注：本文讨论的是 InnorDB的B+Tree索引。</font>
 
> mysql中不同表的相同字段索引是可以重名的，因为索引文件一表一个；命名规则：多个字段用 ＂_＂ 隔开  
> 普通索引：idx_字段名  
> 唯一索引：ux_字段名  

## 1.1 为什么MySQL InnorDB 使用 B+Tree 作为索引数据结构
假设现有数据 主键索引 1,2,3,4,5二叉数

- 二叉树
![](images/ecsjg.png)

- 红黑树
![](images/hhsjg.png)

- B Tree
![](images/b%20tree.png)

- B+Tree
![](images/b+tree.png)

**<font color='red'>总结</font>**
> 1. 二叉树如果存储递增的索引会退化为链表。
> 1. 红黑树的树高比B+树高，IO次数多。
> 1. B树的叶子节点和非叶子节点都有数据所以，B树的层高会大于B+树，B树平均的IO次数会远大于B+树，b+树的数据都集中在叶子节点,非叶子节点只负责索引
> 1. B+数叶子节点的数据是按顺序放置的双向链表，故B+树更擅长支持范围查询，而B树范围查询只能中序遍历。


## 1.2 InnorDB聚簇索引和非聚簇索引
### 1.2.1 聚簇索引

> InnoDB聚簇索引的叶子节点存储行记录，因此， InnoDB必须要有，且只有一个聚集索引：

* 如果表定义了PK，则PK就是聚集索引；
* 如果表没有定义PK，则第一个not NULL unique列是聚集索引；
* 否则，InnoDB会创建一个隐藏的row-id作为聚集索引；

![](images/jucusuoy.png)

### 1.2.2 非聚簇索引

> 也叫普通索引(非主键索引)

![](images/fjcsypng.png)


## 1.3 索引类型

* **主键索引**: 数据列不允许重复，不允许为NULL.一个表只能有一个主键。
* **唯一索引**: 数据列不允许重复，允许为NULL值，一个表允许多个列创建唯一索引
* **普通索引**: 基本的索引类型，没有唯一性的限制，允许为NULL值。
* **全文索引**： 是目前搜索引擎使用的一种关键技术。

**<font color='orange'>上述索引的创建方式:</font>**

* **创建唯一索引**:  ALTER TABLE table_name ADD UNIQUE (column); 
* **创建唯一组合索引**:  ALTER TABLE table_name ADD UNIQUE (column1,column2); 
* **创建普通索引**:  ALTER TABLE table_name ADD INDEX index_name (column); 
* **创建组合索引**: ALTER TABLE table_name ADD INDEX index_name(column1, column2, column3); 
* **创建全文索引**: ALTER TABLE table_name ADD FULLTEXT (column); 


**<font color='orange'>索引的设计原则:</font>**

* 适合索引的列是经常出现在where子句中的列，或者连接子句中指定的列
* 基数较小的列(重复行大)，索引效果较差，没有必要在此列建立索引(例如 status 列)
* 使用短索引，如果对长字符串列进行索引，应该指定一个前缀长度，这样能够节省大量索引空间
* 不要过度索引。索引需要额外的磁盘空间，并降低写操作的性能。在修改表内容的时候，索引会进行更新甚至重构，索引列越多，这个时间就会越长。所以只保持需要的索引有利于查询即可。


## 1.4 索引运用场景

### 1.4.1 覆盖索引与回表查询

- **回表查询**
例如：有一张用户表表结构
```sql
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` varchar(100) NOT NULL COMMENT '姓名',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `code` varchar(100) NOT NULL COMMENT 'code',
   KEY `idx_name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT COMMENT='用户表';
```
用户表的索引如下图所示：  
![](images/fgsy.png)

左边为聚集索引，右边为普通索引

```sql
select * from user where name='ls';
```
该sql查询走索引如下图所示：粉红色路径，需要扫码两遍索引树：
![](images/sycxgc.png)

* 先通过普通索引定位到主键值id=5
* 在通过聚集索引定位到行记录，再拿出所有字段

这就是所谓的回表查询，先定位主键值，再定位行记录，它的性能较扫一遍索引树更低。


- **覆盖索引**
> 只需要在一棵索引树上就能获取SQL所需的所有列数据，无需回表，速度更快，即explain的输出结果Extra字段为Using index时，能够触发索引覆盖。

- **索引下推**

**<font color='red'>待补充</font>**



# 2 索引失效的查询场景

## 2.1 单列索引

### 2.1.1 索引列操作导致索引失效

> 在索引列上进行任何操作，使用函数、计算、类型转换都会导致索引失效，进而进行全表扫描

- **索引列计算：不走索引**

![](images/syjs.png)

- **使用函数：不走索引**

![](images/shjsf.png)

- **类型转换** **<font color='red'>（需要分情况）</font>**

**1. 索引列是数字类型如：int，条件传数字和字符串都能走索引。**


**传数字：<font color='green'>不索引</font>**
![alt](images/szsy_sz.png)


**传字符串：<font color='green'>走索引</font>** 

![alt](images/szsy_zf.png)

**2. 索引列是字符串类型如：varchar，条件传字符串才能走索引。**


**传字符串：<font color='green'>走索引</font>**
![alt](images/zfsy_zf.png)


**传数字：<font color='red'>不走索引</font>**

![alt](images/zfsy_sz.png)

- 2、msyql在使用不等于(!=、<>)的时候会导致索引失效
- 3、is null和is not null也无法使用索引
