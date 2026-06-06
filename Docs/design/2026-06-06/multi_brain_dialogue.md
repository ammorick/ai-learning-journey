# 多大脑并行对话设计草案

> **状态**：早期构思，未在 MVP 中实现。当前版本仅为方向性记录。

## 核心流程

下图展示了未来计划实现的多大脑并行对话机制：多个专家大脑**共享一个框架**，**并行**阅读、思考、生成回答，然后同步更新框架，循环迭代，直到收敛或达到上限。

```mermaid
flowchart TD
    Start([用户问题]) --> Route{路由 & 分层}
    Route -->|简单问题| Direct[直接调用单个专家 → 输出]
    Route -->|复杂问题| Multi[进入多大脑对话]

    subgraph MultiBrain [并行多大脑对话（共享框架）]
        Init[初始化共享框架] --> Pick[随机选择2-3个大脑]
        Pick --> Loop{循环计数 < 上限?<br>且未收敛}
        
        Loop -->|是| Parallel[并行调用]
        
        subgraph ParallelExecution [并行执行]
            direction LR
            B1[大脑A] --> T1[读取框架&生成回答]
            B2[大脑B] --> T2[读取框架&生成回答]
            B3[大脑C] --> T3[读取框架&生成回答]
        end
        
        Parallel --> Sync[同步点：等待所有完成]
        Sync --> Merge[合并结果 → 更新共享框架]
        Merge --> Loop
    end
    
    Loop -->|否| Aggregate[整合最终框架]
    Aggregate --> Final[最终答案]
    Final --> End([返回用户])
    Direct --> End

    subgraph Future [未来可选（暂缓）]
        Contradiction[矛盾大脑] -.->|检测逻辑冲突<br>介入合并阶段| Merge
    end
    ```
    Future -.- Sync