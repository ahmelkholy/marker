---
marp: true
theme: default
size: 16:9
backgroundColor: #f8f9fa
color: #2c3e50
paginate: true
math: katex
footer: "PSE Lecture 7 - Transmission Investment | Kirschen & Strbac"
# 📏 FONT SIZE CONTROL: Change the --font-scale value below to adjust ALL fonts
# --font-scale: 1.0 = Normal size
# --font-scale: 0.8 = 80% smaller (for content-heavy slides)
# --font-scale: 1.2 = 20% larger (for better readability)
style: |
  :root {
    --font-scale: 1;  /* Change this one value to scale all fonts */
  }
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 50px 60px;
    font-size: calc(1.6em * var(--font-scale));  /* Normal base font size */
  }
  h1 {
    color: #2c3e50;
    text-align: center;
    font-size: calc(2.2em * var(--font-scale));  /* Normal title size */
    margin-bottom: 25px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
  }
  h2 {
    color: #34495e;
    border-bottom: 3px solid #3498db;
    padding-bottom: 8px;
    font-size: calc(1.4em * var(--font-scale));  /* Normal heading size */
  }
  h3 {
    color: #2980b9;
    font-size: calc(1.0em * var(--font-scale));  /* Normal subheading size */
  }
  .key-point {
    background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
    color: #2c3e50;
    padding: calc(15px * var(--font-scale));  /* Dynamic padding */
    border-radius: 12px;
    margin: calc(15px * var(--font-scale)) 0;
    box-shadow: 0 6px 24px rgba(0,0,0,0.1);
    font-size: calc(0.9em * var(--font-scale));  /* Dynamic font size */
  }
  .highlight {
    background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
    padding: calc(12px * var(--font-scale));  /* Dynamic padding */
    border-radius: 8px;
    margin: calc(12px * var(--font-scale)) 0;
    font-size: calc(0.9em * var(--font-scale));  /* Dynamic font size */
  }
  .formula {
    background: #ecf0f1;
    border-left: 4px solid #3498db;
    padding: calc(12px * var(--font-scale));  /* Dynamic padding */
    margin: calc(12px * var(--font-scale)) 0;
    font-family: 'Courier New', monospace;
    font-size: calc(0.85em * var(--font-scale));  /* Dynamic font size */
  }
  .warning {
    background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
    color: #2c3e50;
    border-left: 4px solid #ff4500;
    color: white;
    padding: calc(12px * var(--font-scale));  /* Dynamic padding */
    border-radius: 8px;
    margin: calc(12px * var(--font-scale)) 0;
    font-size: calc(0.9em * var(--font-scale));  /* Dynamic font size */
  }
  .two-column {
    display: flex;
    gap: 40px;
  }
  .content-left {
    flex: 1;
  }
  .figure-right {
    flex: 1;
    text-align: center;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    margin: calc(15px * var(--font-scale)) 0;
    font-size: calc(0.8em * var(--font-scale));  /* Dynamic table font */
  }
  th, td {
    border: 1px solid #bdc3c7;
    padding: calc(6px * var(--font-scale));  /* Dynamic padding */
    text-align: center;
    font-size: calc(0.9em * var(--font-scale));  /* Dynamic cell font */
  }
  th {
    background: #3498db;
    color: white;
  }
  .figure-right img {
    max-height: calc(400px * var(--font-scale));  /* Dynamic image height */
    max-width: 100%;
    object-fit: contain;
  }
  ul, ol {
    font-size: calc(0.9em * var(--font-scale));  /* Dynamic list font */
    margin: calc(8px * var(--font-scale)) 0;
    padding-left: calc(25px * var(--font-scale));
  }
  li {
    margin: calc(3px * var(--font-scale)) 0;  /* Dynamic list spacing */
  }
---

# 🚀 Transmission Investment in Power Systems

## 📊 Fundamentals of Power System Economics

### _Strategic Investment Decisions in Competitive Markets_

### _Eng. Mahomoud M. Elkholy_

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

<div class="two-column">
<div class="content-left">

### 🎯 **First Example - Simple Two-Bus System**

**Value Determination:**

- **Bus A**: Generator G1 at 20 $/MWh
- **Bus B**: Generator G2 at 45 $/MWh, Load = 1000 MW
- **Transmission Value** = 45 - 20 = **25 $/MWh**

**Investment Criterion:**
Build transmission if annualized cost < 25 $/MWh

### 💰 **Key Insight**

Transmission competes with local generation - value determined by price differentials

</div>
<div class="figure-right">

![Two-Bus System](_page_7_Figure_1.jpeg)

</div>
</div>

---

## 📈 Borduria-Syldavia Example: Step-by-Step Analysis

<div class="two-column">
<div class="content-left">

### 🔢 **System Parameters**

**Generation Cost Functions:**

- **Borduria**: π_B = 10 + 0.01P_B $/MWh
- **Syldavia**: π_S = 13 + 0.02P_S $/MWh

**Fixed Demands:**

- **Borduria**: 500 MW
- **Syldavia**: 1500 MW

### 💡 **Key Insight**

Borduria has **cheaper generation** but **smaller demand**
Syldavia has **expensive generation** but **larger demand**

</div>
<div class="figure-right">

![Two-Bus System](_page_8_Figure_1.jpeg)

</div>
</div>

---

## 📊 Step 1: Independent Markets (No Interconnection)

### 🔢 **Price Calculations**

**Borduria (isolated):**

- Production = Local demand = 500 MW
- Price = 10 + 0.01(500) = **15 $/MWh**

**Syldavia (isolated):**

- Production = Local demand = 1500 MW
- Price = 13 + 0.02(1500) = **43 $/MWh**

**Price Difference = 43 - 15 = 28 $/MWh**

<div class="key-point">

### 💰 **Economic Interpretation**

This **28 $/MWh** difference represents the **maximum value** of transmitting the first MW from Borduria to Syldavia!

</div>

---

## 🔄 Step 2: Deriving the Transmission Demand Function

<div class="highlight">

### 📈 **As Flow F Increases from Borduria to Syldavia:**

- **Borduria production**: P_B = 500 + F (local + export)
- **Syldavia production**: P_S = 1500 - F (local - import)

</div>

### 🎯 **Mathematical Derivation**

**Transmission Value:**

```
π_T(F) = π_S(F) - π_B(F)
```

**Substituting cost functions:**

```
π_T(F) = [13 + 0.02(1500 - F)] - [10 + 0.01(500 + F)]
π_T(F) = [13 + 30 - 0.02F] - [10 + 5 + 0.01F]
π_T(F) = 43 - 0.02F - 15 - 0.01F
π_T(F) = 28 - 0.03F $/MWh
```

---

## 📍 Step 3: Key Points on the Transmission Demand Curve

<div class="two-column">
<div class="content-left">

### 🎯 **Critical Flow Values**

<div class="highlight">

**At F = 0 MW:**

- π_T = 28 $/MWh
- **Maximum transmission value**

**At F = 933.3 MW:**

- π_T = 0 $/MWh
- **Prices equalize!**

</div>

### 📊 **When Prices Equalize (F = 933.3 MW):**

- **Borduria**: 500 + 933.3 = 1433.3 MW
- **Syldavia**: 1500 - 933.3 = 566.7 MW
- **Both prices**: 24.33 $/MWh

</div>
<div class="content-left">

### 📈 **Economic Logic**

<div class="formula">

**Setting π_T = 0:**

```
28 - 0.03F = 0
F = 28/0.03 = 933.3 MW
```

</div>

Beyond this point, transmission becomes **economically inefficient** - we'd be moving power from high-cost to low-cost areas!

</div>
</div>

---

## ⚖️ Step 4: Optimal Transmission Capacity Determination

### 🎯 **Optimization Rule**

**Optimal Capacity T\***: Marginal Benefit = Marginal Cost
**Marginal Benefit** = Transmission price = π_T(F)
**Marginal Cost** = Long-run marginal cost of transmission

### 🔢 **Given Investment Parameters:**

- **Investment cost**: k = 35 $/MW·km·year
- **Line length**: l = 1000 km
- **Annualized LRMC**: 35 × 1000 ÷ 8760 = **4.00 $/MWh**

**Setting π_T(F) = LRMC:**

```
28 - 0.03F = 4.00
0.03F = 24
F = 800 MW
```

**Therefore: Optimal transmission capacity = 800 MW**

---

## 📊 Step 5: Economic Equilibrium Analysis

<div class="two-column">
<div class="content-left">

### ✅ **At Optimal Capacity (800 MW):**

**Generation Dispatch:**

- **Borduria**: 500 + 800 = 1300 MW
- **Syldavia**: 1500 - 800 = 700 MW

**Prices:**

- **Borduria**: 10 + 0.01(1300) = 23 $/MWh
- **Syldavia**: 13 + 0.02(700) = 27 $/MWh

**Price difference**: 27 - 23 = **4 $/MWh** = LRMC ✅

</div>
<div class="content-left">

### 💰 **Revenue vs Cost Analysis**

**Hourly transmission revenue:**

- 800 MW × 4 $/MWh = **$3,200/hour**

**Annual transmission revenue:**

- $3,200 × 8760 hours = **$28.03M/year**

**Investment cost:**

- 35 × 1000 × 800 = **$28M/year**

**Perfect cost recovery!** 💯

</div>
</div>

---

## 📈 Step 6: Peak/Off-Peak Analysis Setup

<div class="highlight">

### 🕐 **Realistic Load Variation**

Real systems have **time-varying loads** - this significantly affects transmission economics!

**Load Periods:**

- **Peak**: 3889 hours/year, Total load = 3600 MW
- **Off-Peak**: 4871 hours/year, Total load = 600 MW

</div>

### 📊 **Load Distribution by Country**

| Period   | Borduria Load | Syldavia Load | Total Load | Duration (h) |
| -------- | ------------- | ------------- | ---------- | ------------ |
| Peak     | 900 MW        | 2700 MW       | 3600 MW    | 3889         |
| Off-Peak | 150 MW        | 450 MW        | 600 MW     | 4871         |

**Objective:** Balance **annual energy cost savings** vs **annualized transmission cost**

---

## 💰 Step 7: Detailed Analysis - 400 MW Transmission Capacity

<div class="two-column">
<div class="content-left">

### 🔄 **Off-Peak Conditions (4871 hours)**

<div class="highlight">

**No Congestion** - transmission limit not binding

**Economic Dispatch:**

- **Borduria**: 500 MW generation
- **Syldavia**: 100 MW generation
- **Flow**: 350 MW export (< 400 MW limit)

**Market Outcome:**

- **Single market price**: 15.00 $/MWh
- **Congestion revenue**: **$0/hour**

</div>

</div>
<div class="content-left">

### ⚡ **Peak Conditions (3889 hours)**

<div class="highlight">

**Congestion occurs** - 400 MW limit binding

**Constrained Dispatch:**

- **Borduria**: 1300 MW total (900 local + 400 export)
- **Syldavia**: 2300 MW generation

**Market Outcome:**

- **Borduria price**: 23.00 $/MWh
- **Syldavia price**: 59.00 $/MWh
- **Price difference**: 36.00 $/MWh
- **Hourly revenue**: 400 × 36 = **$14,400/hour**

</div>

</div>
</div>

---

## 🎯 Step 8: Revenue Recovery Calculations

<div class="key-point">

### 💰 **Annual Revenue Calculation**

**Off-peak revenue:** $0/hour × 4871 hours = **$0**
**Peak revenue:** $14,400/hour × 3889 hours = **$56,000,000**
**Total annual revenue:** **$56,000,000**

**Investment Cost (400 MW, 140 $/MW·km·year):**
140 × 1000 × 400 = **$56,000,000**

**Result: Perfect 100% cost recovery!** ✅

</div>

### 📊 **Key Economic Insight**

<div class="highlight">

Even though transmission is **free during off-peak**, the **peak congestion revenue** is sufficient to fully recover the investment cost when capacity is optimally sized!

</div>

---

## 📈 Step 9: Over/Under-Investment Analysis

<div class="two-column">
<div class="content-left">

### 📈 **Over-Investment Scenario (500 MW)**

**Peak Analysis:**

- **Flow**: 500 MW (instead of 400 MW)
- **Borduria**: 1400 MW generation
- **Syldavia**: 2200 MW generation
- **Prices**: 24 vs 57 $/MWh
- **Price difference**: 33 $/MWh (vs 36 $/MWh)

**Result:** **Lower congestion = Lower revenue**
Revenue < Investment cost → Poor cost recovery

</div>
<div class="content-left">

### 📉 **Under-Investment Scenario (300 MW)**

**Peak Analysis:**

- **Flow**: 300 MW (constrained)
- **Borduria**: 1200 MW generation
- **Syldavia**: 2400 MW generation
- **Prices**: 22 vs 61 $/MWh
- **Price difference**: 39 $/MWh

**Revenue:** Higher than optimal case
**Investment:** Lower than optimal case
**Result:** **Over-recovery (114%)**

</div>
</div>

### 🎯 **Strategic Implication**

Under-investment can be **financially attractive** but **economically inefficient**!

---

## 🧮 Step 10: Mathematical Summary - **Complete Economic Model**

**Transmission demand function:**

```
π_T(F) = 28 - 0.03F $/MWh
```

**Investment supply function:**

```
LRMC = k × l / 8760 = 4.00 $/MWh (constant)
```

**Optimal capacity (equilibrium):**

```
28 - 0.03T* = 4.00
T* = 800 MW (single-period case)
T* = 400 MW (peak/off-peak case)
```

**Revenue adequacy condition:**

```
Annual congestion surplus = Annual investment cost
```

---

## 🎯 Key Economic Insights from the Analysis

<div class="key-point">

### ✅ **Critical Success Factors**

1. **Price-Based Signals**: Transmission value determined by nodal price differences
2. **Optimal Investment**: Marginal benefit = Marginal cost principle works
3. **Revenue Adequacy**: Congestion pricing can achieve perfect cost recovery
4. **Load Duration Impact**: Peak periods drive most transmission revenue
5. **System Optimization**: Individual rationality aligns with social optimum

</div>

### 🚀 **Practical Applications**

- **Merchant transmission** business case evaluation
- **Regulatory planning** for transmission expansion
- **Market design** for efficient investment signals
- **Financial transmission rights** pricing and allocation

---

## Key Takeaways

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

💡 **Definition**

Reference network = Existing topology + **Optimal transmission capacities**

🔢 **Process**

1. Minimize total system cost
2. Apply security constraints
3. Compare optimal vs actual capacities

</div>

🎯 **Applications**

- **Benchmark** regulatory performance
- **Identify** investment needs
- **Set** performance incentives

---

## 📊 Mathematical Formulation

<div class="two-column">
<div class="content-left">

### 🎯 **Security Constrained OPF**

**Objective:**

```
min Σ(τ_p × Σ(C_g × P_pg)) + Σ(k_b × l_b × T_b)
```

</div>
<div class="content-left">

### ⚖️ **Constraints & Pricing**

**Subject to:**

- Power balance: ΣP_g - ΣP_d = 0
- Flow limits: |F| ≤ T
- Security constraints

**Nodal Price:**

```
π_j = π_system + Σ(sensitivity × shadow_price)
```

</div>
</div>

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

<img src="_page_34_Figure_6.jpeg" alt="IEEE RTS">

</div>
</div>

---

## 📊 Capacity Analysis Results

<div class="two-column">
<div class="content-left">

### 🎯 **Security vs Economic Optimization**

The comparison between transport-only and security-constrained optimization reveals significant differences in required transmission capacities.

### 💡 **Implications**

- **Security constraints** often dominate capacity requirements
- **Pure economic optimization** may underestimate needs
- **Reliability standards** significantly impact investment decisions

</div>
<div class="figure-right">

![Capacity Analysis](_page_35_Figure_1.jpeg)

</div>
</div>

---

## 🚀 Advanced Considerations

<div class="two-column">
<div class="content-left">

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

</div>
<div class="content-left">

### 🎯 **Dynamic Factors**

- Load growth projections
- Distributed generation
- Storage integration
- Demand-side management
- Environmental constraints

</div>
</div>

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
