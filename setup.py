import setuptools


with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="nonebot_plugin_questionmark",
    version="0.3.0",
    author="Number_Sir",
    author_email="Number_Sir@126.com",
    keywords=["pip", "nonebot2", "nonebot", "nonebot_plugin"],
    description="""基于 OneBot 适配器的 NoneBot2 行为艺术插件, 有群友或私聊发送全是问号/感叹号的消息时, bot会自动把问号/感叹号方向翻转并发出来""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NumberSir/nonebot_plugin_questionmark",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'nonebot2>=2.0.0rc3',
    ],
    python_requires=">=3.8"
)
