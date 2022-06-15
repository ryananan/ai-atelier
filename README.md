# AI Alien beta 🤖👾 AI外星人  V0.0.4
###  Access it here 👉 [![Open tool in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oM7eELv6EbL_efnnRyOgBGn1W-PkeaCE#scrollTo=qWpYuD-gm29X) 👈 请点此访问
Based on the Disco Diffusion, we have developed a **Chinese & English version** of the AI art creation software "AI Atelier". We offer both **Text-To-Image** models (Disco Diffusion and VQGAN+CLIP) and **Text-To-Text** (GPT-J-6B and GPT-NEOX-20B) as options.

在Disco Diffusion模型的基础上，我们开发了一款**汉化版AI艺术创作软件“AI聊天画室”**。我们同时提供了**文本生成图像**模型（Disco Diffusion与VQGAN+CLIP）及**文本生成文本**（GPT-J-6B及GPT-NEOX-20B）可供选择。

![visitors](https://visitor-badge.glitch.me/badge?page_id=ai-atlier&left_text=visitors) 
<a href="https://github.com/ryananan/ai-atelier/pulse" alt="Activity">
  <img src="https://img.shields.io/github/commit-activity/m/ryananan/ai-atelier/V0.0.4" /></a>
  
**🌈✨ Welcome the participation of more developers to help making AI Art more accessible ✨🌈**

**🌈✨ 欢迎更多开发者参与并助力ai艺术的普及与发展 ✨🌈**
  
--- 
### 📜 License 许可证 📜 GNU Affero General Public License v3.0

Making available complete source code of licensed works and modifications, which include larger works using a licensed work, `under the same license`. Copyright and license notices must be preserved.  When a modified version is used to provide a service over a network, the complete source code of the modified version must be made available. </br>

如果您将本程序二次开发或者提供给他人使用（即使是仅作为在线工具提供服务），您必须`延用AGPL许可证`且在网上开源共享你修改的版本。相应的版权和许可声明必须保留。

[More info](https://www.gnu.org/licenses/agpl-3.0.en.html) ｜ 相关信息 [[1]](https://machbbs.com/v2ex/375293) [[2]](https://zhuanlan.zhihu.com/p/340135415) 

---

#### 🍻 What's New 新增功能 🍻 
`V0.0.4`<br/>
· Add Chinese translation 新增汉化翻译<br/>
· Add chatbot(text-to-text) generation 新增聊天机器人（文本生成文本） <br/>
· Optimise files saving structure 优化文件保存结构 <br/>
· Update GUI and colour scheme to improve readability 优化界面及色彩主题以提升可读性 <br/>
· Host api for authorization 新增用于授权的API接口 <br/>

`V0.0.3`<br/>
· Save your own settings to google drive 可保存你的参数设置至谷歌云盘<br/>
· Save generated process video to google drive 可将生成过程的视频保存至谷歌云盘 <br/>
· More prompt enhancers 新增风格类形容词 <br/>
· Improve GUI of colab notebook 优化界面排版 <br/>
· Default image size set to 16:9 默认图像尺寸设置为16:9 <br/>
· Fix 'seed' value error  修复 "种子"值不同步的错误<br/>

#### 💭  To-do 待开发 💭
☑️ Buildin GPT-J-6B chatbot  搭建GPT-J-6B聊天机器人 <br/>
· Create 2D and 3D animations and not only still frames (from Disco Diffusion v5 and VQGAN Animations)  创建2D和3D动画，而非静态图像（来自Disco Diffusion v5和VQGAN Animations）<br/>
· Restore your own settings  导入并恢复你的图像设置<br/>
· Input audio and images for generation instead of just text 输入音频和图片进行生成，而不仅仅是文字。<br/>
· Simplify tool setup process on colab, and enable ‘one-click’ sharing of the generated link to other users. Experiment with the possibilities for multi-user access to the same link. 简化colab端工具加载流程，优化链接分享流程。实验允许多个用户接入同个链接使用的可能性。<br/>

---
### 🤹 Credits 致谢 🤹

This would not be possible without the brilliant work of MindsEye beta develop by <a href='https://twitter.com/multimodalart' target='_blank'>@multimodalart</a> and gpt-j-api by <a href='https://github.com/vicgalle' target='_blank'>Víctor Gallego.</a><br>
<a href="https://colab.research.google.com/github/alembics/disco-diffusion/blob/main/Disco_Diffusion.ipynb" target="_blank">Disco Diffusion v5</a> model by <a href="https://twitter.com/somnai_dreams" target="_blank">@somnai_dreams</a> and <a href="https://twitter.com/gandamu" target="_blank">@gandamu</a>, based on the foundational work of <a href="https://twitter.com/RiversHaveWings">@RiversHaveWings</a>, with modifications by <a href="https://twitter.com/danielrussruss" target="_blank">@danielrussruss</a>, <a href="https://github.com/Dango233" target="_blank">Dango233</a>, <a href="https://twitter.com/chigozienri">Chigozie Nri</a>, <a href="https://twitter.com/softologyComAu" target="_blank">@softologyComAu</a> and others.<br><a href="https://colab.research.google.com/drive/1N4UNSbtNMd31N_gAT9rAm8ZzPh62Y5ud" target="_blank">Hypertron v2</a> VQGAN model by <a href="https://github.com/Philipuss1" target="_blank">Philipuss</a> adapted from <a href="https://twitter.com/RiversHaveWings">@RiversHaveWings</a> with modifications by <a href="https://twitter.com/jbusted1">@jbusted1</a>, <a href="https://twitter.com/softologyComAu" target="_blank">@softologyComAu</a> and others. Original GAN+CLIP by <a href="https://twitter.com/advadnoun">@advadnoun</a>. <a href="https://github.com/openai/CLIP" target="_blank">CLIP</a> and <a href="https://github.com/openai/guided-diffusion" target="_blank">Guided Diffusion</a> were originally released by <a href="https://openai.com" target="_blank">OpenAI</a>. <a href="https://github.com/CompVis/taming-transformers" target="_blank">VQGAN</a> was released by <a href="https://github.com/CompVis" target="_blank">CompVis Heidelberg.</a><br>
API access to large language models by <a href="https://textsynth.com/" target="_blank">TextSynth.</a> Translation powered by <a href="https://translate.google.com/" target="_blank">Google</a>. </small><br>

<p>感谢<a href='https://twitter.com/multimodalart' target='_blank'>@multimodalart</a>的MindsEye beta 与 <a href='https://github.com/vicgalle' target='_blank'>Víctor Gallego</a>的gpt-j-api的开创性作品，本软件才能得以实现。<br>
<a href="https://colab.research.google.com/github/alembics/disco-diffusion/blob/main/Disco_Diffusion.ipynb" target="_blank">Disco Diffusion v5</a>模型由<a href="https://twitter.com/somnai_dreams" target="_blank">@somnai_dreams</a>与<a href="https://twitter.com/gandamu" target="_blank">@gandamu</a>所开发。基于<a href="https://twitter.com/RiversHaveWings">@RiversHaveWings</a>开创性的基础工作，以及<a href="https://twitter.com/danielrussruss" target="_blank">@danielrussruss</a>，<a href="https://github.com/Dango233" target="_blank">Dango233</a>，<a href="https://twitter.com/chigozienri">Chigozie Nri</a>，<a href="https://twitter.com/softologyComAu" target="_blank">@softologyComAu</a>等其他人对其进一步的优化。参数的中文翻译基于<a href="https://github.com/Vultur">Vultur</a>。<br>
<a href="https://colab.research.google.com/drive/1N4UNSbtNMd31N_gAT9rAm8ZzPh62Y5ud" target="_blank">Hypertron v2</a>VQGAN 模型由<a href="https://github.com/Philipuss1" target="_blank">Philipuss</a>改编自<a href="https://twitter.com/RiversHaveWings">@RiversHaveWings</a>， 并由<a href="https://twitter.com/jbusted1">@jbusted1</a>和<a href="https://twitter.com/softologyComAu" target="_blank">@softologyComAu</a>等其他人进一步修改。 原始GAN+CLIP由<a href="https://twitter.com/advadnoun">@advadnoun</a>所提供。<a href="https://github.com/openai/CLIP" target="_blank">CLIP</a>和<a href="https://github.com/openai/guided-diffusion" target="_blank">Guided Diffusion</a>最初由<a href="https://openai.com" target="_blank">OpenAI</a>发布。<a href="https://github.com/CompVis/taming-transformers" target="_blank">VQGAN</a>则是由<a href="https://github.com/CompVis" target="_blank">CompVis Heidelberg</a>发布的。<br>
对大型语言模型的API访问由<a href="https://textsynth.com/" target="_blank">TextSynth</a>提供。翻译技术来自<a href="https://translate.google.com/" target="_blank">谷歌


