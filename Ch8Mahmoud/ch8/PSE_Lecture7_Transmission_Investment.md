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
    --font-scale: 1.1;  /* Change this one value to scale all fonts */
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
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
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
    background: linear-gradient(135deg, #ff7675 0%, #fd79a8 100%);
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

```
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

<div class="two-column">
<div class="content-left">

### 🔄 **Off-Peak Conditions**

- **No Congestion** - single market
- **Borduria**: 500 MW gen
- **Syldavia**: 100 MW gen
- **Flow**: 350 MW export
- **Price**: 15.00 $/MWh both
- **Revenue**: **$0/hour**

</div>
<div class="content-left">

### ⚡ **Peak Conditions**

- **Congestion** - limit binding
- **Borduria**: 1300 MW total
- **Syldavia**: 2300 MW gen
- **Prices**: 23 vs 59 $/MWh
- **Value**: 36 $/MWh difference
- **Revenue**: **$14,400/hour**

</div>
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

## 🏗️ Economies of Scale in Transmission

<div class="formula">

### 💰 **Total Investment Cost Structure**

```
C_T(T) = C_F + C_V(T)
```

Where:

- **C_F** = Fixed cost (independent of capacity)
- **C_V(T)** = Variable cost (proportional to capacity)

</div>

### 🎯 **Key Economic Challenge**

<div class="highlight">

Fixed costs don't affect **optimal capacity determination** but significantly impact **revenue adequacy** and cost recovery

</div>

---

## 💡 Capacity Withholding Strategy

<div class="key-point">

### 🔧 **Strategic Behavior**

- **Withholding capacity** increases price differentials
- Can generate **higher revenues** to recover fixed costs
- Creates artificial scarcity for revenue enhancement

</div>

### 📊 **Example Analysis**

**Scenario**: 650 MW capacity available instead of 800 MW optimal

- **Result**: Higher congestion prices
- **Trade-off**: Economic efficiency vs cost recovery
- **Regulatory concern**: Market power abuse

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

<div class="formula">

**Objective:**

```
min Σ(τ_p × Σ(C_g × P_pg)) + Σ(k_b × l_b × T_b)
```

</div>

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
