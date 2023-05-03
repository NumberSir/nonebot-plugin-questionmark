<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
  
# Nonebot_Plugin_QuestionMark
  
_✨ 基于OneBot适配器的[NoneBot2](https://v2.nonebot.dev/)行为艺术插件 ✨_
  
</div>

## 功能

有群友或私聊发送全是问号`?`,`？`或`¿`或感叹号`!`,`！`,`¡`的消息时, bot会自动把问号/感叹号翻转方向发出去


## 安装

- 使用 nb-cli

```
nb plugin install nonebot_plugin_questionmark
```

- 使用 pip

```
pip install -U nonebot_plugin_questionmark
```

## 配置项
```ini
QM_TRIGGER_RATE=0.3                # 触发回复概率，默认 0.3
QM_ENABLE_GROUPS=[12345, 114514, "all"]   # 白名单群聊，仅列表内群聊可能触发回复；当列表内为 "all" 时所有群聊均启用
```

## 图片示例

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/227783077-b490dad2-5e1a-42eb-b455-53f381934497.png" width="500" />
</div>

## 更新日志
> 2023-05-03 v0.4.1
> - 优化白名单 [@issue/3](https://github.com/NumberSir/nonebot-plugin-questionmark/issues/3)
>
> 2023-05-02 v0.4.0
> - 添加概率触发回复功能
> - 添加白名单群聊(仅qq可用)功能 [@issue/3](https://github.com/NumberSir/nonebot-plugin-questionmark/issues/3)
> 
> 2023-04-02 v0.3.1
> - 修bug
> 
> 2023-03-29 v0.3.0
> - 优化实现
>
> 2023-03-27 v0.2.1
> - 优化实现
> - 添加感叹号
> 
> 2023-03-26 v0.1.0
> - 发布
