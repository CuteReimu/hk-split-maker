# hk-split-maker

代码全部来源自[github.com/slaurent22/hk-split-maker](https://github.com/slaurent22/hk-split-maker)，本人将其进行了汉化。

联动项目：Golang编写的带有窗口界面的[CuteReimu/hksplitmaker](https://github.com/CuteReimu/hksplitmaker) （仅支持Windows系统）

## 如何为汉化做贡献

因为参与汉化的朋友很多都不懂如何使用Github，以下内容主要针对Github的使用。**如果能熟练使用Github的朋友无需往下看了。**

1. Fork （因为你没有这个仓库的直接编辑权限）
  - 如果你是第一次为这个项目做贡献，请点击右上角三个按钮中的`Fork`按钮，这将会把本仓库拷贝一份到你的账户下。点击这个按钮后会自动跳转到你的账户下拷贝的那份仓库里，你可以在自己账户下的仓库随意编辑。
  - 如果你曾经已经Fork过了，点击`Fork`按钮也会自动跳转到你账户下拷贝的那份仓库里。

2. 在中间偏上方的位置，确定你现在是在master分支（只要不乱点，一般就是的）

![image](https://user-images.githubusercontent.com/77955264/150159712-36f3af43-22e0-4e27-a2cb-5d2a7c69e4d4.png)

3. 再往下一排，你会看到：
  > This branch is up to date with CuteReimu:master
   
   并且右边会有两个按钮。点击`Fetch upstream`，然后点击`Fetch and merge`，会将这个仓库的最新版本同步到你自己的仓库下面。（如果`Fetch and merge`按钮不能点，并且有提示'No new commit to fetch. Enjoy your day!'，说明已经同步到最新版本了）

4. 点击上方的`Actions`按钮，你会看到中间有一个很大的按钮

   ![image](https://user-images.githubusercontent.com/77955264/150159972-beb8e2fa-57d3-42aa-ae4c-8b684bb47f7a.png)

点击这个按钮。（这一步如果你之前曾经做过，就不需要再做一次了）

5. 点击左上角的`Code`按钮，回到代码页，再次确定一下你是在master分支（只要不乱点，一般就是的）

![image](https://user-images.githubusercontent.com/77955264/150159712-36f3af43-22e0-4e27-a2cb-5d2a7c69e4d4.png)

6. 在文件列表里找到`translate.tsv`并打开，点击右上角像笔一样的按钮，这个就是编辑按钮，然后你就可以编辑这个文件了。因为是在你自己的仓库里，所以你可以自由地编辑。英文和中文之间用tab隔开。但是如果你仅仅按tab键的话，Github会“贴心地”用几个空格代替你的tab，而这并不是我们想要的。所以你可以考虑把内容全部复制粘贴到自己电脑的文本编辑器下面，修改完成后再复制粘贴回来。

7. 之后随意在下方输入一些提交信息，你就可以提交了。注意按照下图的选项：

![image](https://user-images.githubusercontent.com/77955264/150160711-93d77792-1d20-4918-8fc2-2f7ddbb627ab.png)

8. 再次点击左上角的`Code`按钮，回到**你自己仓库的**代码页。稍等一两分钟，刷新几次页面，等到这个小黄点变成绿勾后

![image](https://user-images.githubusercontent.com/77955264/150162638-94b38f5d-a75e-4bf7-b4ae-656fcdf9c634.png)

再稍等一两分钟，你会看到右下角的

![image](https://user-images.githubusercontent.com/77955264/150162991-0659ac37-833b-4c22-9149-d4384fa3f8fe.png)

点击这个github-pages。

![image](https://user-images.githubusercontent.com/77955264/150163361-005f451f-3dbb-4cd0-8a7f-efbdd88e08a3.png)

如果你看到最近的这个提交，是几分钟前(minutes ago)或者几秒钟前(seconds ago)，说明部署好了。点击右边的`View deployment`按钮可以预览你的更新（如果没有更新，可以按ctrl+F5强制刷新一下试试）。

9. 确认无误后，再次回到你的代码页，找到那一排
  > This branch is up to date with CuteReimu:master.

  点击右边的`Contribute`按钮，然后点击`Open pull request`按钮。随意输入一些合并信息，然后点击`Create pull request`按钮，就可以申请将你的仓库下的修改合并回这个仓库了。
