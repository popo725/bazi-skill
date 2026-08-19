# Third-Party Notices / 第三方代码与许可证说明

本文件用于商业化前的代码来源审计。任何外部代码进入生产环境前，必须再次核对上游仓库当时的许可证版本、版权声明和依赖许可证。

## 1. jinchenma94/bazi-skill

- 来源：https://github.com/jinchenma94/bazi-skill
- 当前仓库关系：本仓库为其 Fork。
- 许可证：MIT License。
- 用途：现有八字 Skill、排盘脚本、参考规则。
- 商业使用原则：允许在 MIT 条款下使用、修改和分发；必须保留许可证和版权声明。

## 2. 6tail/lunar-python

- 来源：https://github.com/6tail/lunar-python
- 许可证：MIT License。
- 计划用途：中国历法、农历/公历、干支等交叉核验和基础能力。
- 集成方式：优先作为依赖使用，不整仓复制；通过 Adapter 与本项目隔离。
- 商业使用原则：保留 MIT LICENSE / NOTICE。

## 3. SylarLong/iztro

- 来源：https://github.com/SylarLong/iztro
- 许可证：MIT License。
- 计划用途：紫微斗数排盘基础。
- 集成方式：优先 npm 依赖；服务端封装为结构化 API。
- 商业使用原则：保留 MIT LICENSE / NOTICE。

## 4. HeiGeAi/HeiGe-SuanMing

- 来源：https://github.com/HeiGeAi/HeiGe-SuanMing
- 许可证：PolyForm Noncommercial License 1.0.0。
- 结论：**不得直接进入本商业项目生产代码。**
- 允许：研究功能列表、测试组织方式、模块化思想。
- 禁止：复制源码、修改后商用、将其脚本混入收费产品。
- 替代方案：梅花、六爻、奇门等模块基于传统公开规则 clean-room 独立实现；若未来需要直接使用，应取得作者单独商业授权。

## 5. china-testing/bazi

- 来源：https://github.com/china-testing/bazi
- GitHub 当前未声明明确开源许可证。
- 结论：**不能默认复制并商用。**
- 允许：研究公开功能和产品思路。
- 替代方案：从公共领域古籍、公开传统规则和自有设计重新实现所需功能；若要复制代码，先取得版权方明确授权。

## 6. 商业代码准入规则

第三方代码进入主分支前必须满足以下之一：

1. MIT / BSD / Apache-2.0 等明确允许商业使用的许可证，且已保留 NOTICE；
2. 已获得版权所有人书面商业授权；
3. 由本项目依据公开规则 clean-room 独立实现，并保留实现依据和测试证明。

未经确认许可证的 GitHub 公共仓库不得因为“能看到源码”就复制进商业项目。
