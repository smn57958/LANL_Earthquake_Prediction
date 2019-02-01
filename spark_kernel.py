Microsoft Windows [Version 10.0.17763.292]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\Sohan Nipunage>spark-shell
2019-01-31 23:25:31 ERROR Shell:397 - Failed to locate the winutils binary in the hadoop binary path
java.io.IOException: Could not locate executable C:\Hadoop\bin\bin\winutils.exe in the Hadoop binaries.
        at org.apache.hadoop.util.Shell.getQualifiedBinPath(Shell.java:379)
        at org.apache.hadoop.util.Shell.getWinUtilsPath(Shell.java:394)
        at org.apache.hadoop.util.Shell.<clinit>(Shell.java:387)
        at org.apache.hadoop.util.StringUtils.<clinit>(StringUtils.java:80)
        at org.apache.hadoop.security.SecurityUtil.getAuthenticationMethod(SecurityUtil.java:611)
        at org.apache.hadoop.security.UserGroupInformation.initialize(UserGroupInformation.java:273)
        at org.apache.hadoop.security.UserGroupInformation.ensureInitialized(UserGroupInformation.java:261)
        at org.apache.hadoop.security.UserGroupInformation.loginUserFromSubject(UserGroupInformation.java:791)
        at org.apache.hadoop.security.UserGroupInformation.getLoginUser(UserGroupInformation.java:761)
        at org.apache.hadoop.security.UserGroupInformation.getCurrentUser(UserGroupInformation.java:634)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at scala.Option.getOrElse(Option.scala:121)
        at org.apache.spark.util.Utils$.getCurrentUserName(Utils.scala:2422)
        at org.apache.spark.SecurityManager.<init>(SecurityManager.scala:79)
        at org.apache.spark.deploy.SparkSubmit.secMgr$lzycompute$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$secMgr$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at scala.Option.map(Option.scala:146)
        at org.apache.spark.deploy.SparkSubmit.prepareSubmitEnvironment(SparkSubmit.scala:366)
        at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:143)
        at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:86)
        at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:924)
        at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:933)
        at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
2019-01-31 23:25:31 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://SOHAN-HP:4040
Spark context available as 'sc' (master = local[*], app id = local-1548995142336).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.4.0
      /_/

Using Scala version 2.11.12 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_171)
Type in expressions to have them evaluated.
Type :help for more information.

scala> pyspark
<console>:24: error: not found: value pyspark
       pyspark
       ^

scala> exit
<console>:24: error: not found: value exit
       exit
       ^

scala> exit()
<console>:24: error: not found: value exit
       exit()
       ^

scala> close
<console>:24: error: not found: value close
       close
       ^

scala> Terminate batch job (Y/N)?
^CTerminate batch job (Y/N)? Y

C:\Users\Sohan Nipunage>pyspark
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
2019-01-31 23:33:23 ERROR Shell:397 - Failed to locate the winutils binary in the hadoop binary path
java.io.IOException: Could not locate executable C:\Hadoop\bin\bin\winutils.exe in the Hadoop binaries.
        at org.apache.hadoop.util.Shell.getQualifiedBinPath(Shell.java:379)
        at org.apache.hadoop.util.Shell.getWinUtilsPath(Shell.java:394)
        at org.apache.hadoop.util.Shell.<clinit>(Shell.java:387)
        at org.apache.hadoop.util.StringUtils.<clinit>(StringUtils.java:80)
        at org.apache.hadoop.security.SecurityUtil.getAuthenticationMethod(SecurityUtil.java:611)
        at org.apache.hadoop.security.UserGroupInformation.initialize(UserGroupInformation.java:273)
        at org.apache.hadoop.security.UserGroupInformation.ensureInitialized(UserGroupInformation.java:261)
        at org.apache.hadoop.security.UserGroupInformation.loginUserFromSubject(UserGroupInformation.java:791)
        at org.apache.hadoop.security.UserGroupInformation.getLoginUser(UserGroupInformation.java:761)
        at org.apache.hadoop.security.UserGroupInformation.getCurrentUser(UserGroupInformation.java:634)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at scala.Option.getOrElse(Option.scala:121)
        at org.apache.spark.util.Utils$.getCurrentUserName(Utils.scala:2422)
        at org.apache.spark.SecurityManager.<init>(SecurityManager.scala:79)
        at org.apache.spark.deploy.SparkSubmit.secMgr$lzycompute$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$secMgr$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at scala.Option.map(Option.scala:146)
        at org.apache.spark.deploy.SparkSubmit.prepareSubmitEnvironment(SparkSubmit.scala:366)
        at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:143)
        at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:86)
        at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:924)
        at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:933)
        at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
2019-01-31 23:33:23 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.0
      /_/

Using Python version 3.6.4 (v3.6.4:d48eceb, Dec 19 2017 06:54:40)
SparkSession available as 'spark'.
>>> print("Hello")
Hello
>>> import pandas as pd
>>> data=pd.read_csv("C:\Users\Sohan Nipunage\Dropbox\LANL_kaggle\LANL_Earthquake_Prediction\train.csv")
  File "<stdin>", line 1
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> exit()

C:\Users\Sohan Nipunage>SUCCESS: The process with PID 3024 (child process of PID 7708) has been terminated.
SUCCESS: The process with PID 7708 (child process of PID 12252) has been terminated.
SUCCESS: The process with PID 12252 (child process of PID 12532) has been terminated.


C:\Users\Sohan Nipunage>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Sohan Nipunage>cd Desktop

C:\Users\Sohan Nipunage\Desktop>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Sohan Nipunage\Desktop>cd "C:\Users\Sohan Nipunage\Dropbox\LANL_kaggle\LANL_Earthquake_Prediction"

C:\Users\Sohan Nipunage\Dropbox\LANL_kaggle\LANL_Earthquake_Prediction>dir
 Volume in drive C is Windows
 Volume Serial Number is 5480-3884

 Directory of C:\Users\Sohan Nipunage\Dropbox\LANL_kaggle\LANL_Earthquake_Prediction

01/31/2019  09:34 AM    <DIR>          .
01/31/2019  09:34 AM    <DIR>          ..
01/31/2019  09:27 AM               329 .gitignore
01/31/2019  06:39 PM               135 kernel_1.py
01/31/2019  09:26 AM             1,092 LICENSE
01/31/2019  09:26 AM                96 README.md
01/10/2019  01:12 AM     9,555,558,244 train.csv
01/31/2019  09:21 AM     2,175,592,057 train.csv.zip
               6 File(s) 11,731,151,953 bytes
               2 Dir(s)  77,690,695,680 bytes free

C:\Users\Sohan Nipunage\Dropbox\LANL_kaggle\LANL_Earthquake_Prediction>pyspark kernel_1.py
Running python applications through 'pyspark' is not supported as of Spark 2.0.
Use ./bin/spark-submit <python file>

C:\Users\Sohan Nipunage\Dropbox\LANL_kaggle\LANL_Earthquake_Prediction>pyspark
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
2019-01-31 23:36:05 ERROR Shell:397 - Failed to locate the winutils binary in the hadoop binary path
java.io.IOException: Could not locate executable C:\Hadoop\bin\bin\winutils.exe in the Hadoop binaries.
        at org.apache.hadoop.util.Shell.getQualifiedBinPath(Shell.java:379)
        at org.apache.hadoop.util.Shell.getWinUtilsPath(Shell.java:394)
        at org.apache.hadoop.util.Shell.<clinit>(Shell.java:387)
        at org.apache.hadoop.util.StringUtils.<clinit>(StringUtils.java:80)
        at org.apache.hadoop.security.SecurityUtil.getAuthenticationMethod(SecurityUtil.java:611)
        at org.apache.hadoop.security.UserGroupInformation.initialize(UserGroupInformation.java:273)
        at org.apache.hadoop.security.UserGroupInformation.ensureInitialized(UserGroupInformation.java:261)
        at org.apache.hadoop.security.UserGroupInformation.loginUserFromSubject(UserGroupInformation.java:791)
        at org.apache.hadoop.security.UserGroupInformation.getLoginUser(UserGroupInformation.java:761)
        at org.apache.hadoop.security.UserGroupInformation.getCurrentUser(UserGroupInformation.java:634)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at scala.Option.getOrElse(Option.scala:121)
        at org.apache.spark.util.Utils$.getCurrentUserName(Utils.scala:2422)
        at org.apache.spark.SecurityManager.<init>(SecurityManager.scala:79)
        at org.apache.spark.deploy.SparkSubmit.secMgr$lzycompute$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$secMgr$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at scala.Option.map(Option.scala:146)
        at org.apache.spark.deploy.SparkSubmit.prepareSubmitEnvironment(SparkSubmit.scala:366)
        at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:143)
        at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:86)
        at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:924)
        at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:933)
        at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
2019-01-31 23:36:05 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.0
      /_/

Using Python version 3.6.4 (v3.6.4:d48eceb, Dec 19 2017 06:54:40)
SparkSession available as 'spark'.
>>> import pandas as pd
>>> data=pd.read_csv("train.csv")
Terminate batch job (Y/N)? ERROR:py4j.java_gateway:An error occurred while trying to connect to the Java server (127.0.0.1:50424)
Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1145, in send_command
    self.socket.sendall(command.encode("utf-8"))
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 985, in send_command
    response = connection.send_command(command)
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1149, in send_command
    "Error while sending", e, proto.ERROR_ON_SEND)
py4j.protocol.Py4JNetworkError: Error while sending

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 929, in _get_connection
    connection = self.deque.pop()
IndexError: pop from an empty deque

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1067, in start
    self.socket.connect((self.address, self.port))
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1145, in send_command
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 985, in send_command
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1149, in send_command
py4j.protocol.Py4JNetworkError: Error while sending

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 929, in _get_connection
IndexError: pop from an empty deque

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1067, in start
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python36\lib\site-packages\pandas\io\parsers.py", line 709, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Python36\lib\site-packages\pandas\io\parsers.py", line 455, in _read
    data = parser.read(nrows)
  File "C:\Python36\lib\site-packages\pandas\io\parsers.py", line 1069, in read
    ret = self._engine.read(nrows)
  File "C:\Python36\lib\site-packages\pandas\io\parsers.py", line 1839, in read
    data = self._reader.read(nrows)
  File "pandas\_libs\parsers.pyx", line 902, in pandas._libs.parsers.TextReader.read
  File "pandas\_libs\parsers.pyx", line 952, in pandas._libs.parsers.TextReader._read_low_memory
  File "pandas\_libs\parsers.pyx", line 2225, in pandas._libs.parsers._concatenate_chunks
  File "C:\Python36\lib\site-packages\pandas\core\dtypes\common.py", line 478, in is_categorical_dtype
    def is_categorical_dtype(arr_or_dtype):
  File "C:\SPARK\python\pyspark\context.py", line 251, in signal_handler
    self.cancelAllJobs()
  File "C:\SPARK\python\pyspark\context.py", line 1021, in cancelAllJobs
    self._jsc.sc().cancelAllJobs()
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1255, in __call__
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1000, in send_command
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 983, in send_command
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 931, in _get_connection
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 937, in _create_connection
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1079, in start
py4j.protocol.Py4JNetworkError: An error occurred while trying to connect to the Java server (127.0.0.1:50424)
>>> dataRDD=spark.textfile("train.csv")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SparkSession' object has no attribute 'textfile'
>>> dataRDD=spark.textFile("train.csv")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SparkSession' object has no attribute 'textFile'
>>> rdd=spark.textFile()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SparkSession' object has no attribute 'textFile'
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> exit()
ERROR:py4j.java_gateway:An error occurred while trying to connect to the Java server (127.0.0.1:50424)
Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 929, in _get_connection
    connection = self.deque.pop()
IndexError: pop from an empty deque

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1067, in start
    self.socket.connect((self.address, self.port))
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
C:\SPARK\python\pyspark\context.py:428: RuntimeWarning: Unable to cleanly shutdown Spark JVM process. It is possible that the process has crashed, been killed or may also be in a zombie state.
  RuntimeWarning

Terminate batch job (Y/N)?
ERROR: The process with PID 13176 (child process of PID 236) could not be terminated.
Reason: The operation attempted is not supported.
ERROR: The process with PID 236 (child process of PID 1312) could not be terminated.
Reason: The operation attempted is not supported.
Terminate batch job (Y/N)? Y
Terminate batch job (Y/N)? Y

C:\Users\Sohan Nipunage\Dropbox\LANL_kaggle\LANL_Earthquake_Prediction>spark-shell
2019-01-31 23:50:34 ERROR Shell:397 - Failed to locate the winutils binary in the hadoop binary path
java.io.IOException: Could not locate executable C:\Hadoop\bin\bin\winutils.exe in the Hadoop binaries.
        at org.apache.hadoop.util.Shell.getQualifiedBinPath(Shell.java:379)
        at org.apache.hadoop.util.Shell.getWinUtilsPath(Shell.java:394)
        at org.apache.hadoop.util.Shell.<clinit>(Shell.java:387)
        at org.apache.hadoop.util.StringUtils.<clinit>(StringUtils.java:80)
        at org.apache.hadoop.security.SecurityUtil.getAuthenticationMethod(SecurityUtil.java:611)
        at org.apache.hadoop.security.UserGroupInformation.initialize(UserGroupInformation.java:273)
        at org.apache.hadoop.security.UserGroupInformation.ensureInitialized(UserGroupInformation.java:261)
        at org.apache.hadoop.security.UserGroupInformation.loginUserFromSubject(UserGroupInformation.java:791)
        at org.apache.hadoop.security.UserGroupInformation.getLoginUser(UserGroupInformation.java:761)
        at org.apache.hadoop.security.UserGroupInformation.getCurrentUser(UserGroupInformation.java:634)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at scala.Option.getOrElse(Option.scala:121)
        at org.apache.spark.util.Utils$.getCurrentUserName(Utils.scala:2422)
        at org.apache.spark.SecurityManager.<init>(SecurityManager.scala:79)
        at org.apache.spark.deploy.SparkSubmit.secMgr$lzycompute$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$secMgr$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at scala.Option.map(Option.scala:146)
        at org.apache.spark.deploy.SparkSubmit.prepareSubmitEnvironment(SparkSubmit.scala:366)
        at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:143)
        at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:86)
        at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:924)
        at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:933)
        at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
2019-01-31 23:50:34 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://SOHAN-HP:4040
Spark context available as 'sc' (master = local[*], app id = local-1548996644629).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.4.0
      /_/

Using Scala version 2.11.12 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_171)
Type in expressions to have them evaluated.
Type :help for more information.

scala> exit
<console>:24: error: not found: value exit
       exit
       ^

scala> Terminate batch job (Y/N)? y
Terminate batch job (Y/N)? y

C:\Users\Sohan Nipunage\Dropbox\LANL_kaggle\LANL_Earthquake_Prediction>pyspark
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
2019-01-31 23:51:07 ERROR Shell:397 - Failed to locate the winutils binary in the hadoop binary path
java.io.IOException: Could not locate executable C:\Hadoop\bin\bin\winutils.exe in the Hadoop binaries.
        at org.apache.hadoop.util.Shell.getQualifiedBinPath(Shell.java:379)
        at org.apache.hadoop.util.Shell.getWinUtilsPath(Shell.java:394)
        at org.apache.hadoop.util.Shell.<clinit>(Shell.java:387)
        at org.apache.hadoop.util.StringUtils.<clinit>(StringUtils.java:80)
        at org.apache.hadoop.security.SecurityUtil.getAuthenticationMethod(SecurityUtil.java:611)
        at org.apache.hadoop.security.UserGroupInformation.initialize(UserGroupInformation.java:273)
        at org.apache.hadoop.security.UserGroupInformation.ensureInitialized(UserGroupInformation.java:261)
        at org.apache.hadoop.security.UserGroupInformation.loginUserFromSubject(UserGroupInformation.java:791)
        at org.apache.hadoop.security.UserGroupInformation.getLoginUser(UserGroupInformation.java:761)
        at org.apache.hadoop.security.UserGroupInformation.getCurrentUser(UserGroupInformation.java:634)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
        at scala.Option.getOrElse(Option.scala:121)
        at org.apache.spark.util.Utils$.getCurrentUserName(Utils.scala:2422)
        at org.apache.spark.SecurityManager.<init>(SecurityManager.scala:79)
        at org.apache.spark.deploy.SparkSubmit.secMgr$lzycompute$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$secMgr$1(SparkSubmit.scala:359)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:367)
        at scala.Option.map(Option.scala:146)
        at org.apache.spark.deploy.SparkSubmit.prepareSubmitEnvironment(SparkSubmit.scala:366)
        at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:143)
        at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:86)
        at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:924)
        at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:933)
        at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
2019-01-31 23:51:07 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.0
      /_/

Using Python version 3.6.4 (v3.6.4:d48eceb, Dec 19 2017 06:54:40)
SparkSession available as 'spark'.
>>> data=sc.textFile("train.csv")
>>> print(data.head())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'RDD' object has no attribute 'head'
>>> dataframe=spark.createDataFrame(data)
[Stage 0:>                                                          (0 + 1) / 1]Traceback (most recent call last):
  File "C:\Python36\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "C:\Python36\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\SPARK\python\lib\pyspark.zip\pyspark\worker.py", line 25, in <module>
ModuleNotFoundError: No module named 'resource'
2019-01-31 23:56:16 ERROR Executor:91 - Exception in task 0.0 in stage 0.0 (TID 0)
org.apache.spark.SparkException: Python worker failed to connect back.
        at org.apache.spark.api.python.PythonWorkerFactory.createSimpleWorker(PythonWorkerFactory.scala:170)
        at org.apache.spark.api.python.PythonWorkerFactory.create(PythonWorkerFactory.scala:97)
        at org.apache.spark.SparkEnv.createPythonWorker(SparkEnv.scala:117)
        at org.apache.spark.api.python.BasePythonRunner.compute(PythonRunner.scala:108)
        at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:65)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:324)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:288)
        at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:90)
        at org.apache.spark.scheduler.Task.run(Task.scala:121)
        at org.apache.spark.executor.Executor$TaskRunner$$anonfun$10.apply(Executor.scala:402)
        at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1360)
        at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:408)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:748)
Caused by: java.net.SocketTimeoutException: Accept timed out
        at java.net.DualStackPlainSocketImpl.waitForNewConnection(Native Method)
        at java.net.DualStackPlainSocketImpl.socketAccept(DualStackPlainSocketImpl.java:135)
        at java.net.AbstractPlainSocketImpl.accept(AbstractPlainSocketImpl.java:409)
        at java.net.PlainSocketImpl.accept(PlainSocketImpl.java:199)
        at java.net.ServerSocket.implAccept(ServerSocket.java:545)
        at java.net.ServerSocket.accept(ServerSocket.java:513)
        at org.apache.spark.api.python.PythonWorkerFactory.createSimpleWorker(PythonWorkerFactory.scala:164)
        ... 14 more
2019-01-31 23:56:16 WARN  TaskSetManager:66 - Lost task 0.0 in stage 0.0 (TID 0, localhost, executor driver): org.apache.spark.SparkException: Python worker failed to connect back.
        at org.apache.spark.api.python.PythonWorkerFactory.createSimpleWorker(PythonWorkerFactory.scala:170)
        at org.apache.spark.api.python.PythonWorkerFactory.create(PythonWorkerFactory.scala:97)
        at org.apache.spark.SparkEnv.createPythonWorker(SparkEnv.scala:117)
        at org.apache.spark.api.python.BasePythonRunner.compute(PythonRunner.scala:108)
        at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:65)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:324)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:288)
        at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:90)
        at org.apache.spark.scheduler.Task.run(Task.scala:121)
        at org.apache.spark.executor.Executor$TaskRunner$$anonfun$10.apply(Executor.scala:402)
        at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1360)
        at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:408)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:748)
Caused by: java.net.SocketTimeoutException: Accept timed out
        at java.net.DualStackPlainSocketImpl.waitForNewConnection(Native Method)
        at java.net.DualStackPlainSocketImpl.socketAccept(DualStackPlainSocketImpl.java:135)
        at java.net.AbstractPlainSocketImpl.accept(AbstractPlainSocketImpl.java:409)
        at java.net.PlainSocketImpl.accept(PlainSocketImpl.java:199)
        at java.net.ServerSocket.implAccept(ServerSocket.java:545)
        at java.net.ServerSocket.accept(ServerSocket.java:513)
        at org.apache.spark.api.python.PythonWorkerFactory.createSimpleWorker(PythonWorkerFactory.scala:164)
        ... 14 more

2019-01-31 23:56:16 ERROR TaskSetManager:70 - Task 0 in stage 0.0 failed 1 times; aborting job
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\session.py", line 746, in createDataFrame
    rdd, schema = self._createFromRDD(data.map(prepare), schema, samplingRatio)
  File "C:\SPARK\python\pyspark\sql\session.py", line 390, in _createFromRDD
    struct = self._inferSchema(rdd, samplingRatio, names=schema)
  File "C:\SPARK\python\pyspark\sql\session.py", line 361, in _inferSchema
    first = rdd.first()
  File "C:\SPARK\python\pyspark\rdd.py", line 1378, in first
    rs = self.take(1)
  File "C:\SPARK\python\pyspark\rdd.py", line 1360, in take
    res = self.context.runJob(self, takeUpToNumLeft, p)
  File "C:\SPARK\python\pyspark\context.py", line 1051, in runJob
    sock_info = self._jvm.PythonRDD.runJob(self._jsc.sc(), mappedRDD._jrdd, partitions)
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1257, in __call__
  File "C:\SPARK\python\pyspark\sql\utils.py", line 63, in deco
    return f(*a, **kw)
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\protocol.py", line 328, in get_return_value
py4j.protocol.Py4JJavaError: An error occurred while calling z:org.apache.spark.api.python.PythonRDD.runJob.
: org.apache.spark.SparkException: Job aborted due to stage failure: Task 0 in stage 0.0 failed 1 times, most recent failure: Lost task 0.0 in stage 0.0 (TID 0, localhost, executor driver): org.apache.spark.SparkException: Python worker failed to connect back.
        at org.apache.spark.api.python.PythonWorkerFactory.createSimpleWorker(PythonWorkerFactory.scala:170)
        at org.apache.spark.api.python.PythonWorkerFactory.create(PythonWorkerFactory.scala:97)
        at org.apache.spark.SparkEnv.createPythonWorker(SparkEnv.scala:117)
        at org.apache.spark.api.python.BasePythonRunner.compute(PythonRunner.scala:108)
        at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:65)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:324)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:288)
        at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:90)
        at org.apache.spark.scheduler.Task.run(Task.scala:121)
        at org.apache.spark.executor.Executor$TaskRunner$$anonfun$10.apply(Executor.scala:402)
        at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1360)
        at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:408)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:748)
Caused by: java.net.SocketTimeoutException: Accept timed out
        at java.net.DualStackPlainSocketImpl.waitForNewConnection(Native Method)
        at java.net.DualStackPlainSocketImpl.socketAccept(DualStackPlainSocketImpl.java:135)
        at java.net.AbstractPlainSocketImpl.accept(AbstractPlainSocketImpl.java:409)
        at java.net.PlainSocketImpl.accept(PlainSocketImpl.java:199)
        at java.net.ServerSocket.implAccept(ServerSocket.java:545)
        at java.net.ServerSocket.accept(ServerSocket.java:513)
        at org.apache.spark.api.python.PythonWorkerFactory.createSimpleWorker(PythonWorkerFactory.scala:164)
        ... 14 more

Driver stacktrace:
        at org.apache.spark.scheduler.DAGScheduler.org$apache$spark$scheduler$DAGScheduler$$failJobAndIndependentStages(DAGScheduler.scala:1887)
        at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1875)
        at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1874)
        at scala.collection.mutable.ResizableArray$class.foreach(ResizableArray.scala:59)
        at scala.collection.mutable.ArrayBuffer.foreach(ArrayBuffer.scala:48)
        at org.apache.spark.scheduler.DAGScheduler.abortStage(DAGScheduler.scala:1874)
        at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:926)
        at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:926)
        at scala.Option.foreach(Option.scala:257)
        at org.apache.spark.scheduler.DAGScheduler.handleTaskSetFailed(DAGScheduler.scala:926)
        at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.doOnReceive(DAGScheduler.scala:2108)
        at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:2057)
        at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:2046)
        at org.apache.spark.util.EventLoop$$anon$1.run(EventLoop.scala:49)
        at org.apache.spark.scheduler.DAGScheduler.runJob(DAGScheduler.scala:737)
        at org.apache.spark.SparkContext.runJob(SparkContext.scala:2061)
        at org.apache.spark.SparkContext.runJob(SparkContext.scala:2082)
        at org.apache.spark.SparkContext.runJob(SparkContext.scala:2101)
        at org.apache.spark.api.python.PythonRDD$.runJob(PythonRDD.scala:153)
        at org.apache.spark.api.python.PythonRDD.runJob(PythonRDD.scala)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
        at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:357)
        at py4j.Gateway.invoke(Gateway.java:282)
        at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
        at py4j.commands.CallCommand.execute(CallCommand.java:79)
        at py4j.GatewayConnection.run(GatewayConnection.java:238)
        at java.lang.Thread.run(Thread.java:748)
Caused by: org.apache.spark.SparkException: Python worker failed to connect back.
        at org.apache.spark.api.python.PythonWorkerFactory.createSimpleWorker(PythonWorkerFactory.scala:170)
        at org.apache.spark.api.python.PythonWorkerFactory.create(PythonWorkerFactory.scala:97)
        at org.apache.spark.SparkEnv.createPythonWorker(SparkEnv.scala:117)
        at org.apache.spark.api.python.BasePythonRunner.compute(PythonRunner.scala:108)
        at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:65)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:324)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:288)
        at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:90)
        at org.apache.spark.scheduler.Task.run(Task.scala:121)
        at org.apache.spark.executor.Executor$TaskRunner$$anonfun$10.apply(Executor.scala:402)
        at org.apache.spark.util.Utils$.tryWithSafeFinally(Utils.scala:1360)
        at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:408)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        ... 1 more
Caused by: java.net.SocketTimeoutException: Accept timed out
        at java.net.DualStackPlainSocketImpl.waitForNewConnection(Native Method)
        at java.net.DualStackPlainSocketImpl.socketAccept(DualStackPlainSocketImpl.java:135)
        at java.net.AbstractPlainSocketImpl.accept(AbstractPlainSocketImpl.java:409)
        at java.net.PlainSocketImpl.accept(PlainSocketImpl.java:199)
        at java.net.ServerSocket.implAccept(ServerSocket.java:545)
        at java.net.ServerSocket.accept(ServerSocket.java:513)
        at org.apache.spark.api.python.PythonWorkerFactory.createSimpleWorker(PythonWorkerFactory.scala:164)
        ... 14 more

>>> data=sc.read.format("csv").load("train.csv")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SparkContext' object has no attribute 'read'
>>> data=spark.read.format("csv").load("train.csv")
>>> print(data.head())
Row(_c0='acoustic_data', _c1='time_to_failure')
>>> print(data[:6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\dataframe.py", line 1289, in __getitem__
    raise TypeError("unexpected item type: %s" % type(item))
TypeError: unexpected item type: <class 'slice'>
>>> print(data.shape)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\dataframe.py", line 1300, in __getattr__
    "'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
AttributeError: 'DataFrame' object has no attribute 'shape'
>>> print(data.shape())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\dataframe.py", line 1300, in __getattr__
    "'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
AttributeError: 'DataFrame' object has no attribute 'shape'
>>> print(data.type())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\dataframe.py", line 1300, in __getattr__
    "'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
AttributeError: 'DataFrame' object has no attribute 'type'
>>> print(data)
DataFrame[_c0: string, _c1: string]
>>> data.index()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\dataframe.py", line 1300, in __getattr__
    "'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
AttributeError: 'DataFrame' object has no attribute 'index'
>>> data.index
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\dataframe.py", line 1300, in __getattr__
    "'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
AttributeError: 'DataFrame' object has no attribute 'index'
>>> data.values.flatten()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\dataframe.py", line 1300, in __getattr__
    "'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
AttributeError: 'DataFrame' object has no attribute 'values'
>>> data.count()
629145481
>>> data.columns
['_c0', '_c1']
>>> data.select("*")
DataFrame[_c0: string, _c1: string]
>>> data.select("_c0")
DataFrame[_c0: string]
>>> data.select("_c0").show
<bound method DataFrame.show of DataFrame[_c0: string]>
>>> data.select("_c0").show()
+-------------+
|          _c0|
+-------------+
|acoustic_data|
|           12|
|            6|
|            8|
|            5|
|            8|
|            8|
|            9|
|            7|
|           -5|
|            3|
|            5|
|            2|
|            2|
|            3|
|           -1|
|            5|
|            6|
|            4|
|            3|
+-------------+
only showing top 20 rows

>>> data.select(data.columns).show()
+-------------+---------------+
|          _c0|            _c1|
+-------------+---------------+
|acoustic_data|time_to_failure|
|           12|   1.4690999832|
|            6|   1.4690999821|
|            8|    1.469099981|
|            5|   1.4690999799|
|            8|   1.4690999788|
|            8|   1.4690999777|
|            9|   1.4690999766|
|            7|   1.4690999755|
|           -5|   1.4690999744|
|            3|   1.4690999733|
|            5|   1.4690999722|
|            2|   1.4690999711|
|            2|     1.46909997|
|            3|   1.4690999689|
|           -1|   1.4690999678|
|            5|   1.4690999667|
|            6|   1.4690999656|
|            4|   1.4690999645|
|            3|   1.4690999634|
+-------------+---------------+
only showing top 20 rows

>>> data.columns
['_c0', '_c1']
>>> data.select(data.columns).show()
+-------------+---------------+
|          _c0|            _c1|
+-------------+---------------+
|acoustic_data|time_to_failure|
|           12|   1.4690999832|
|            6|   1.4690999821|
|            8|    1.469099981|
|            5|   1.4690999799|
|            8|   1.4690999788|
|            8|   1.4690999777|
|            9|   1.4690999766|
|            7|   1.4690999755|
|           -5|   1.4690999744|
|            3|   1.4690999733|
|            5|   1.4690999722|
|            2|   1.4690999711|
|            2|     1.46909997|
|            3|   1.4690999689|
|           -1|   1.4690999678|
|            5|   1.4690999667|
|            6|   1.4690999656|
|            4|   1.4690999645|
|            3|   1.4690999634|
+-------------+---------------+
only showing top 20 rows

>>> data.createOrReplaceTempView("acoustic")
>>> sqlDF=spark.sql("select top 5 * from acoustic")
Traceback (most recent call last):
  File "C:\SPARK\python\pyspark\sql\utils.py", line 63, in deco
    return f(*a, **kw)
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\protocol.py", line 328, in get_return_value
py4j.protocol.Py4JJavaError: An error occurred while calling o25.sql.
: org.apache.spark.sql.catalyst.parser.ParseException:
mismatched input '5' expecting <EOF>(line 1, pos 11)

== SQL ==
select top 5 * from acoustic
-----------^^^

        at org.apache.spark.sql.catalyst.parser.ParseException.withCommand(ParseDriver.scala:241)
        at org.apache.spark.sql.catalyst.parser.AbstractSqlParser.parse(ParseDriver.scala:117)
        at org.apache.spark.sql.execution.SparkSqlParser.parse(SparkSqlParser.scala:48)
        at org.apache.spark.sql.catalyst.parser.AbstractSqlParser.parsePlan(ParseDriver.scala:69)
        at org.apache.spark.sql.SparkSession.sql(SparkSession.scala:642)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
        at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:357)
        at py4j.Gateway.invoke(Gateway.java:282)
        at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
        at py4j.commands.CallCommand.execute(CallCommand.java:79)
        at py4j.GatewayConnection.run(GatewayConnection.java:238)
        at java.lang.Thread.run(Thread.java:748)


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\session.py", line 767, in sql
    return DataFrame(self._jsparkSession.sql(sqlQuery), self._wrapped)
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1257, in __call__
  File "C:\SPARK\python\pyspark\sql\utils.py", line 73, in deco
    raise ParseException(s.split(': ', 1)[1], stackTrace)
pyspark.sql.utils.ParseException: "\nmismatched input '5' expecting <EOF>(line 1, pos 11)\n\n== SQL ==\nselect top 5 * from acoustic\n-----------^^^\n"
>>> sqlDF=spark.sql("select * from acoustic")
2019-02-01 00:18:52 WARN  ObjectStore:6666 - Version information not found in metastore. hive.metastore.schema.verification is not enabled so recording the schema version 1.2.0
2019-02-01 00:18:52 WARN  ObjectStore:568 - Failed to get database default, returning NoSuchObjectException
Traceback (most recent call last):
  File "C:\SPARK\python\pyspark\sql\utils.py", line 63, in deco
    return f(*a, **kw)
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\protocol.py", line 328, in get_return_value
py4j.protocol.Py4JJavaError: An error occurred while calling o25.sql.
: org.apache.spark.sql.AnalysisException: java.lang.RuntimeException: java.io.IOException: (null) entry in command string: null chmod 0733 C:\tmp\hive;
        at org.apache.spark.sql.hive.HiveExternalCatalog.withClient(HiveExternalCatalog.scala:106)
        at org.apache.spark.sql.hive.HiveExternalCatalog.databaseExists(HiveExternalCatalog.scala:214)
        at org.apache.spark.sql.internal.SharedState.externalCatalog$lzycompute(SharedState.scala:114)
        at org.apache.spark.sql.internal.SharedState.externalCatalog(SharedState.scala:102)
        at org.apache.spark.sql.internal.SharedState.globalTempViewManager$lzycompute(SharedState.scala:141)
        at org.apache.spark.sql.internal.SharedState.globalTempViewManager(SharedState.scala:136)
        at org.apache.spark.sql.hive.HiveSessionStateBuilder$$anonfun$2.apply(HiveSessionStateBuilder.scala:55)
        at org.apache.spark.sql.hive.HiveSessionStateBuilder$$anonfun$2.apply(HiveSessionStateBuilder.scala:55)
        at org.apache.spark.sql.catalyst.catalog.SessionCatalog.globalTempViewManager$lzycompute(SessionCatalog.scala:91)
        at org.apache.spark.sql.catalyst.catalog.SessionCatalog.globalTempViewManager(SessionCatalog.scala:91)
        at org.apache.spark.sql.catalyst.catalog.SessionCatalog.lookupRelation(SessionCatalog.scala:696)
        at org.apache.spark.sql.catalyst.analysis.Analyzer$ResolveRelations$.org$apache$spark$sql$catalyst$analysis$Analyzer$ResolveRelations$$lookupTableFromCatalog(Analyzer.scala:730)
        at org.apache.spark.sql.catalyst.analysis.Analyzer$ResolveRelations$.resolveRelation(Analyzer.scala:685)
        at org.apache.spark.sql.catalyst.analysis.Analyzer$ResolveRelations$$anonfun$apply$8.applyOrElse(Analyzer.scala:715)
        at org.apache.spark.sql.catalyst.analysis.Analyzer$ResolveRelations$$anonfun$apply$8.applyOrElse(Analyzer.scala:708)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$$anonfun$resolveOperatorsUp$1$$anonfun$apply$1.apply(AnalysisHelper.scala:90)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$$anonfun$resolveOperatorsUp$1$$anonfun$apply$1.apply(AnalysisHelper.scala:90)
        at org.apache.spark.sql.catalyst.trees.CurrentOrigin$.withOrigin(TreeNode.scala:70)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$$anonfun$resolveOperatorsUp$1.apply(AnalysisHelper.scala:89)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$$anonfun$resolveOperatorsUp$1.apply(AnalysisHelper.scala:86)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$.allowInvokingTransformsInAnalyzer(AnalysisHelper.scala:194)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$class.resolveOperatorsUp(AnalysisHelper.scala:86)
        at org.apache.spark.sql.catalyst.plans.logical.LogicalPlan.resolveOperatorsUp(LogicalPlan.scala:29)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$$anonfun$resolveOperatorsUp$1$$anonfun$1.apply(AnalysisHelper.scala:87)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$$anonfun$resolveOperatorsUp$1$$anonfun$1.apply(AnalysisHelper.scala:87)
        at org.apache.spark.sql.catalyst.trees.TreeNode$$anonfun$4.apply(TreeNode.scala:326)
        at org.apache.spark.sql.catalyst.trees.TreeNode.mapProductIterator(TreeNode.scala:187)
        at org.apache.spark.sql.catalyst.trees.TreeNode.mapChildren(TreeNode.scala:324)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$$anonfun$resolveOperatorsUp$1.apply(AnalysisHelper.scala:87)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$$anonfun$resolveOperatorsUp$1.apply(AnalysisHelper.scala:86)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$.allowInvokingTransformsInAnalyzer(AnalysisHelper.scala:194)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$class.resolveOperatorsUp(AnalysisHelper.scala:86)
        at org.apache.spark.sql.catalyst.plans.logical.LogicalPlan.resolveOperatorsUp(LogicalPlan.scala:29)
        at org.apache.spark.sql.catalyst.analysis.Analyzer$ResolveRelations$.apply(Analyzer.scala:708)
        at org.apache.spark.sql.catalyst.analysis.Analyzer$ResolveRelations$.apply(Analyzer.scala:654)
        at org.apache.spark.sql.catalyst.rules.RuleExecutor$$anonfun$execute$1$$anonfun$apply$1.apply(RuleExecutor.scala:87)
        at org.apache.spark.sql.catalyst.rules.RuleExecutor$$anonfun$execute$1$$anonfun$apply$1.apply(RuleExecutor.scala:84)
        at scala.collection.LinearSeqOptimized$class.foldLeft(LinearSeqOptimized.scala:124)
        at scala.collection.immutable.List.foldLeft(List.scala:84)
        at org.apache.spark.sql.catalyst.rules.RuleExecutor$$anonfun$execute$1.apply(RuleExecutor.scala:84)
        at org.apache.spark.sql.catalyst.rules.RuleExecutor$$anonfun$execute$1.apply(RuleExecutor.scala:76)
        at scala.collection.immutable.List.foreach(List.scala:392)
        at org.apache.spark.sql.catalyst.rules.RuleExecutor.execute(RuleExecutor.scala:76)
        at org.apache.spark.sql.catalyst.analysis.Analyzer.org$apache$spark$sql$catalyst$analysis$Analyzer$$executeSameContext(Analyzer.scala:127)
        at org.apache.spark.sql.catalyst.analysis.Analyzer.execute(Analyzer.scala:121)
        at org.apache.spark.sql.catalyst.analysis.Analyzer$$anonfun$executeAndCheck$1.apply(Analyzer.scala:106)
        at org.apache.spark.sql.catalyst.analysis.Analyzer$$anonfun$executeAndCheck$1.apply(Analyzer.scala:105)
        at org.apache.spark.sql.catalyst.plans.logical.AnalysisHelper$.markInAnalyzer(AnalysisHelper.scala:201)
        at org.apache.spark.sql.catalyst.analysis.Analyzer.executeAndCheck(Analyzer.scala:105)
        at org.apache.spark.sql.execution.QueryExecution.analyzed$lzycompute(QueryExecution.scala:57)
        at org.apache.spark.sql.execution.QueryExecution.analyzed(QueryExecution.scala:55)
        at org.apache.spark.sql.execution.QueryExecution.assertAnalyzed(QueryExecution.scala:47)
        at org.apache.spark.sql.Dataset$.ofRows(Dataset.scala:79)
        at org.apache.spark.sql.SparkSession.sql(SparkSession.scala:642)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
        at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:357)
        at py4j.Gateway.invoke(Gateway.java:282)
        at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
        at py4j.commands.CallCommand.execute(CallCommand.java:79)
        at py4j.GatewayConnection.run(GatewayConnection.java:238)
        at java.lang.Thread.run(Thread.java:748)
Caused by: java.lang.RuntimeException: java.io.IOException: (null) entry in command string: null chmod 0733 C:\tmp\hive
        at org.apache.hadoop.hive.ql.session.SessionState.start(SessionState.java:522)
        at org.apache.spark.sql.hive.client.HiveClientImpl.newState(HiveClientImpl.scala:183)
        at org.apache.spark.sql.hive.client.HiveClientImpl.<init>(HiveClientImpl.scala:117)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
        at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
        at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
        at org.apache.spark.sql.hive.client.IsolatedClientLoader.createClient(IsolatedClientLoader.scala:272)
        at org.apache.spark.sql.hive.HiveUtils$.newClientForMetadata(HiveUtils.scala:384)
        at org.apache.spark.sql.hive.HiveUtils$.newClientForMetadata(HiveUtils.scala:286)
        at org.apache.spark.sql.hive.HiveExternalCatalog.client$lzycompute(HiveExternalCatalog.scala:66)
        at org.apache.spark.sql.hive.HiveExternalCatalog.client(HiveExternalCatalog.scala:65)
        at org.apache.spark.sql.hive.HiveExternalCatalog$$anonfun$databaseExists$1.apply$mcZ$sp(HiveExternalCatalog.scala:215)
        at org.apache.spark.sql.hive.HiveExternalCatalog$$anonfun$databaseExists$1.apply(HiveExternalCatalog.scala:215)
        at org.apache.spark.sql.hive.HiveExternalCatalog$$anonfun$databaseExists$1.apply(HiveExternalCatalog.scala:215)
        at org.apache.spark.sql.hive.HiveExternalCatalog.withClient(HiveExternalCatalog.scala:97)
        ... 64 more
Caused by: java.io.IOException: (null) entry in command string: null chmod 0733 C:\tmp\hive
        at org.apache.hadoop.util.Shell$ShellCommandExecutor.execute(Shell.java:770)
        at org.apache.hadoop.util.Shell.execCommand(Shell.java:866)
        at org.apache.hadoop.util.Shell.execCommand(Shell.java:849)
        at org.apache.hadoop.fs.RawLocalFileSystem.setPermission(RawLocalFileSystem.java:733)
        at org.apache.hadoop.fs.RawLocalFileSystem.mkOneDirWithMode(RawLocalFileSystem.java:491)
        at org.apache.hadoop.fs.RawLocalFileSystem.mkdirsWithOptionalPermission(RawLocalFileSystem.java:532)
        at org.apache.hadoop.fs.RawLocalFileSystem.mkdirs(RawLocalFileSystem.java:509)
        at org.apache.hadoop.fs.FilterFileSystem.mkdirs(FilterFileSystem.java:305)
        at org.apache.hadoop.hive.ql.exec.Utilities.createDirsWithPermission(Utilities.java:3679)
        at org.apache.hadoop.hive.ql.session.SessionState.createRootHDFSDir(SessionState.java:597)
        at org.apache.hadoop.hive.ql.session.SessionState.createSessionDirs(SessionState.java:554)
        at org.apache.hadoop.hive.ql.session.SessionState.start(SessionState.java:508)
        ... 79 more


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\SPARK\python\pyspark\sql\session.py", line 767, in sql
    return DataFrame(self._jsparkSession.sql(sqlQuery), self._wrapped)
  File "C:\SPARK\python\lib\py4j-0.10.7-src.zip\py4j\java_gateway.py", line 1257, in __call__
  File "C:\SPARK\python\pyspark\sql\utils.py", line 69, in deco
    raise AnalysisException(s.split(': ', 1)[1], stackTrace)
pyspark.sql.utils.AnalysisException: 'java.lang.RuntimeException: java.io.IOException: (null) entry in command string: null chmod 0733 C:\\tmp\\hive;'
>>> from pyspark.ml.evaluation import RegressionEvaluator
>>> from pyspark.ml.regression import LinearRegression
>>> from pyspark.ml.tuning import ParamFridBuilder, TrainValidationSplit
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'ParamFridBuilder'
>>> from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit
>>> train,test=data.randomSplit([0.9,0.1],seed=12345)
>>>
