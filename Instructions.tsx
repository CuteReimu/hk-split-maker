import React from "react";

const Instructions: React.FC = () => {
  return (
    <div id="instructions">
      <h2>声明</h2>
      本网页是在<a href="https://hksplitmaker.com/" target="_self" rel="external">原英文版网页</a>的基础上进行了汉化。
      请大家对<a href="https://hksplitmaker.com/" target="_self" rel="external">原英文版网页</a>多多支持。
      <h2>使用方法</h2>
      <ol>
        <li>选择一个模板。</li>
        <li>你可以自定义增加、删除、修改片段，或者调整顺序。你可以自由修改其它内容，或者稍后也可以在LiveSplit中进行进一步修改。</li>
        <li>点击“生成”按钮，生成后的内容将会展示在右侧。检查无误后，点击“下载”按钮，保存到本地。</li>
      </ol>
    </div>
  );
};

export default Instructions;
