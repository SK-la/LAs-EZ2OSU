# LA's EZ2OSU
这是一个.BMSON to .OSU的转换工具，
目前支持：
  1. bmson 5/7/9/14 K 转 .osu;
  2. 可选的去除空轨; 
     对于10K +，将向上取整留出空列，如：16K, 识别应去除3空轨，则转换后是14K，第14轨为空
  3. 可选的是否转换图片、音频;
     输出文件夹中，谱面根目录下将生成art - title.ext格式的图片、主音频，图片后缀带有难度区分
  4. 可选的保留scratch, panel(EZ2AC专属中间轨);
     设置保留时，去除空轨功能会保留对应轨道，无论里面是否有note
  5. 自定义HP, OD, Creator, Source, Tags等
  6. 可自选生成谱包，如MAPPER's - Source PACK
  7. 支持文件夹拖入识别路径
  8. 带有文件树结构预览，自动更新
  9. 软件关闭时记忆设置
      
未来计划功能维护：
  1. 背景音采样转换
  2. 按照bms的内容，将未使用的channels混音进主音频中，即不同难度有不同的主音频
  3. 在文件树结构预览中，支持右键菜单，如选择转换谱面或音频、删除文件、使用编辑器打开谱面文件等
  4. .osu to .osu的功能性谱面转换、信息维护
  5. 支持锁定K数; 无论如何，生成的谱面始终都是锁定的K数（处理逻辑待定）
  6. 可视化的 n to n K：通过鼠标拖动轨道移动, 通过双击轨道定义目标轨道使用的编号；
  7. 可保留预设模版，（下拉栏/滚动窗口）JSON/XML/INI/YAML那种好?
  8. 支持EZ2CATCH

未来计划大版本更新（可能会咕）：
  1. 创建做谱逻辑模版
  2. 创建和弦音组，通过模版设置生成空白midi文件
  3. 通过文件预生成全key音谱面模版，之后自己重排键型就可以了
