# Git 学习实践笔记
## Git 学习笔记
1. Git 是分布式版本控制工具。
2. 核心作用：管理代码版本、回溯、协作。
3. 常用命令：git init、git add、git commit、git push、git log。

## 实践流程
1. 安装 Git 并配置用户名、邮箱
2. 创建文件夹，git init 初始化仓库
3. 编写代码并多次提交
4. 完善 README 文档

## 提交记录
1. 创建 README.md
2. 实现数字点击窗口
3. 添加坐标系
4. 添加三点画三角形
5. 添加 Git 学习笔记
6. 完善实践流程与提交记录
7. 添加问题与解决方法
8. 添加学习心得

## 遇到的问题及解决方法 
1. 问题：命令输入错误，Git Bash 卡住 解决：按 Ctrl+C 中断，重新输入正确命令 
2. 问题：不明白 commit 是什么 解决：commit 就是保存一个版本，方便以后回溯
3. 问题：不会粘贴命令 解决：shift+insert粘贴或者按鼠标中间的滚轮
4. 问题：git commit 时报错，提示 nothing to commit 解决：说明没有修改文件，必须先修改代码或文档，再执行 git add . 才能提交 
5. 问题：运行Python代码时报错，提示 no module named 'tkinter' 解决：这是Python缺少图形库，重新安装Python时勾选“Add to PATH”并安装完整版本