---
marp: true
theme: default
size: 16:9
backgroundColor: #f8f9fa
color: #2c3e50
paginate: true
math: katex
footer: "PSE Lecture 7 - Transmission Investment | Kirschen & Strbac"
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 40px 60px;
    font-size: 0.95em;
  }
  h1 {
    color: #2c3e50;
    text-align: center;
    font-size: 2.5em;
    margin-bottom: 30px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
  }
  h2 {
    color: #34495e;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
    font-size: 1.8em;
  }
  h3 {
    color: #2980b9;
    font-size: 1.4em;
  }
  .key-point {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 15px;
    margin: 20px 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
  }
  .highlight {
    background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
    padding: 15px;
    border-radius: 10px;
    margin: 15px 0;
  }
  .formula {
    background: #ecf0f1;
    border-left: 5px solid #3498db;
    padding: 15px;
    margin: 15px 0;
    font-family: 'Courier New', monospace;
  }
  .warning {
    background: linear-gradient(135deg, #ff7675 0%, #fd79a8 100%);
    color: white;
    padding: 15px;
    border-radius: 10px;
    margin: 15px 0;
  }
  .two-column {
    display: flex;
    gap: 30px;
    align-items: flex-start;
  }
  .content-left {
    flex: 1;
    font-size: 0.9em;
  }
  .figure-right {
    flex: 1;
    text-align: center;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
  }
  th, td {
    border: 1px solid #bdc3c7;
    padding: 8px;
    text-align: center;
  }
  th {
    background: #3498db;
    color: white;
  }
---

# 🚀 Transmission Investment in Power Systems

## 📊 Fundamentals of Power System Economics

### _Strategic Investment Decisions in Competitive Markets_

### _PSE Lecture 7 - Kirschen & Strbac_

---

## 🎯 Transmission Network Expansion

<div class="key-point">

### 🔧 **Core Concepts**

- **Construction** of new lines or **upgrade** existing facilities
- **Increases** secure power trading capacity
- **Expands** generator and consumer participation
- **Requires** economic justification and coordination

</div>

### ⚡ **Two Investment Drivers**

- **Market Forces** → Competition-driven expansion
- **Regulation** → Monopoly transmission companies need oversight

---

## 🏗️ Nature of Transmission Business

### 🔍 **Key Characteristics**

<div class="highlight">

### 📍 **Rationale**

Exists because generators and users are in different locations

### 🏢 **Natural Monopoly**

- Minimum efficient scale is very large
- Environmental constraints prevent competition

### 💰 **Capital Intensive**

- High upfront costs, low operating costs
- Investment decisions are critical

</div>

---

## 🏗️ Transmission Business Characteristics

<div class="two-column">
<div class="content-left">

### ⏰ **Long Asset Life**

- **20-40+ years** equipment lifespan
- Economic conditions change significantly
- **Stranded investment** risk

### 🚫 **Irreversible Investments**

- Cannot redeploy elsewhere
- Low resale value
- Must live with consequences

</div>
<div class="content-left">

### 📦 **Lumpy Investments**

- Standardized equipment ratings
- Large, infrequent investments
- Cannot exactly match demand

### 📈 **Economies of Scale**

- Fixed costs independent of capacity
- Average cost ↓ with capacity ↑

</div>
</div>

---

## 💡 Quantifying Transmission Value

### 🎯 **First Example - Simple Two-Bus System**

<div class="formula">

**Value Determination:**

- **Bus A**: Generator G1 at 20 $/MWh
- **Bus B**: Generator G2 at 45 $/MWh, Load = 1000 MW
- **Transmission Value** = 45 - 20 = **25 $/MWh**

**Investment Criterion:**
Build transmission if annualized cost < 25 $/MWh

</div>

### 💰 **Key Insight**

Transmission competes with local generation - value determined by price differentials

---

## 📈 Borduria-Syldavia Example

<div class="two-column">
<div class="content-left">

### 🔢 **System Parameters**

**Generation Cost Functions:**

- **Borduria**: π_B = 10 + 0.01P_B $/MWh
- **Syldavia**: π_S = 13 + 0.02P_S $/MWh

**Demands:**

- **Borduria**: 500 MW
- **Syldavia**: 1500 MW

</div>
<div class="figure-right">

![Two-Bus System](_page_7_Figure_1.jpeg)

</div>
</div>

### 🎯 **Transmission Demand Function**

```math
π_T(F) = 28 - 0.03F $/MWh
```

---

## 📊 Optimal Transmission Capacity

<div class="key-point">

### ⚖️ **Optimization Criterion**

**Optimal Capacity T\***: Marginal Benefit = Marginal Cost

Where:

- **Marginal Benefit** = Reduction in congestion cost
- **Marginal Cost** = Annualized investment cost per MW

</div>

### 🔢 **For Borduria-Syldavia:**

- **Optimal Flow**: 933.3 MW (when prices equalize)
- **Transmission Price**: π_T = 28 - 0.03F
- **Optimal Investment**: When π_T = Long-run marginal cost

---

## 📈 Third Example: Peak/Off-Peak Analysis

<div class="highlight">

### 🕐 **Load Periods**

- **Peak**: 3889 hours, Load = 3600 MW
- **Off-Peak**: 4871 hours, Load = 600 MW
- **Objective**: Balance annual energy cost savings vs annualized transmission cost

</div>

### 📊 **Load Duration Approach**

| Period   | Borduria Load | Syldavia Load | Duration (h) |
| -------- | ------------- | ------------- | ------------ |
| Peak     | 900 MW        | 2700 MW       | 3889         |
| Off-Peak | 150 MW        | 450 MW        | 4871         |

---

## 💰 Example: 400 MW Transmission Capacity

### 🔄 **Off-Peak Conditions**

<div class="formula">

- **No Congestion** - markets operate as single system
- **Borduria**: 500 MW generation, **Syldavia**: 100 MW
- **Flow**: 350 MW to Syldavia
- **Prices**: 15.00 $/MWh in both regions
- **Congestion Revenue**: **$0/hour**

</div>

### ⚡ **Peak Conditions**

<div class="formula">

- **Congestion occurs** - transmission limit binding
- **Borduria**: 1300 MW (900 local + 400 export)
- **Syldavia**: 2300 MW generation
- **Prices**: 23.00 $/MWh (Borduria), 59.00 $/MWh (Syldavia)
- **Congestion Value**: 36.00 $/MWh
- **Hourly Revenue**: 400 × 36 = **$14,400/hour**

</div>

---

## 🎯 Revenue Recovery Analysis

### 📊 **Optimal vs Actual Capacity**

<div class="two-column">
<div class="content-left">

### ✅ **Optimal Case (400 MW)**

- **Annual Revenue**: $56M
- **Investment Cost**: $56M
- **Recovery**: 100%

### 📈 **Over-investment (500 MW)**

- **Peak Revenue**: $33/MWh vs $36/MWh
- **Reduced congestion** = **Lower revenue**

</div>
<div class="content-left">

### 📉 **Under-investment (300 MW)**

- **Off-peak Revenue**: $450/hour
- **Peak Revenue**: $11,700/hour
- **Annual Revenue**: $47.7M
- **Investment Cost**: $42M
- **Over-recovery**: 114%

</div>
</div>

---

## 🏗️ Economies of Scale Effects

<div class="formula">

### 💰 **Total Investment Cost**

```math
C_T(T) = C_F + C_V(T)
```

Where:

- **C_F** = Fixed cost (independent of capacity)
- **C_V(T)** = Variable cost (proportional to capacity)

### 🎯 **Key Challenge**

Fixed costs don't affect optimal capacity but affect revenue adequacy

</div>

### 💡 **Capacity Withholding Strategy**

- Withholding capacity increases price differentials
- Can generate higher revenues to recover fixed costs
- **Example**: 650 MW available instead of 800 MW optimal

---

## 🔗 Three-Bus System Complexity

<div class="warning">

### ⚡ **Kirchhoff's Law Effects**

- Power flows follow **physical laws**, not contracts
- Congestion on one line affects **entire network** prices
- Individual line revenues ≠ Individual line costs
- **Total** congestion surplus = **Total** investment cost

</div>

### 📋 **Key Result**

Even though individual lines may not achieve cost recovery, the **total system** achieves perfect cost recovery under optimal design.

---

## 🎯 Reference Network Concept

<div class="key-point">

### 💡 **Definition**

Reference network = Existing topology + **Optimal transmission capacities**

### 🎯 **Applications**

- **Benchmark** for regulatory performance
- **Identify** investment needs
- **Detect** stranded investments
- **Set** performance incentives

</div>

### 🔢 **Optimization Process**

1. Minimize total system cost (operation + investment)
2. Subject to security constraints
3. Determine optimal capacity for each line
4. Compare with actual capacities

---

## 📊 Mathematical Formulation

<div class="formula">

### 🎯 **Security Constrained OPF**

**Objective:**

```math
min Σ(τ_p × Σ(C_g × P_pg)) + Σ(k_b × l_b × T_b)
```

**Subject to:**

- **Power balance**: ΣP_g - ΣP_d = 0
- **Flow equations**: F = H(P_g - P_d)
- **Capacity limits**: |F| ≤ T
- **Security constraints**: All contingencies

</div>

### ⚖️ **Nodal Price Calculation**

```math
π_j = π_system + Σ(sensitivity × shadow_price)
```

---

## 📈 IEEE RTS Case Study

<div class="two-column">
<div class="content-left">

### 🏗️ **24-Bus Test System Results**

<div class="highlight">

### 🔍 **Key Finding**

Most lines require **much higher capacity** for security than for pure transport

**Transport vs Security:**

- Transport needs: ~20-50% of optimal
- Security needs: 100% of optimal capacity

</div>

</div>
<div class="figure-right">

![IEEE RTS](_page_34_Figure_6.jpeg)

![Capacity Analysis](_page_35_Figure_1.jpeg)

</div>
</div>

---

## 🚀 Advanced Considerations

### 🔮 **Implementation Challenges**

<div class="highlight">

### 📈 **Revenue Adequacy**

- Fixed costs recovery
- Capacity withholding strategies
- Regulatory mechanisms

### ⚡ **Network Effects**

- Topology optimization
- Voltage level selection
- FACTS devices integration

</div>

### 🎯 **Dynamic Factors**

- **Load growth projections** • **Distributed generation**
- **Storage integration** • **Demand-side management**
- **Environmental constraints**

---

## 📋 Problem Set Example

### 📊 **Three-Period Load Analysis**

| Period | Load A (MW) | Load B (MW) | Duration (h) |
| ------ | ----------- | ----------- | ------------ |
| High   | 4,000       | 2,000       | 1,000        |
| Medium | 2,200       | 1,100       | 5,000        |
| Low    | 1,000       | 500         | 2,760        |

### 🎯 **Analysis Tasks**

1. Calculate **optimal transmission capacity**
2. Compare **congestion revenue** with **investment cost**
3. Analyze **±33.3% capacity scenarios**

---

## 🎓 Key Takeaways

<div class="key-point">

### ✅ **Critical Success Factors**

1. **Economic Optimization**: Balance constraint costs vs investment costs
2. **Revenue Recovery**: Congestion surplus should match investment costs
3. **Security Requirements**: Often drive capacity needs more than economics
4. **System-wide View**: Individual line economics vs total system optimization
5. **Regulatory Framework**: Need proper incentives for optimal investment

</div>

### 🚀 **Future Directions**

Market-based transmission investment, merchant transmission, performance-based regulation

---

## 📚 Conclusion

### 🎯 **Strategic Insights**

- **Transmission investment** requires careful **economic analysis**
- **Optimal capacity** balances **operational efficiency** and **investment costs**
- **Revenue recovery** through **congestion pricing** provides market signals
- **System-wide optimization** essential for **economic efficiency**
- **Regulatory frameworks** must encourage **optimal investment decisions**

<div class="highlight">

### 💡 **Final Message**

Effective transmission investment coordination is crucial for competitive electricity markets to deliver maximum economic welfare to society.

</div>
