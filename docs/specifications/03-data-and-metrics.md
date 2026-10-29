# Data contract and metric semantics

## Required discovery gate

Source target: `bigquery-public-data.thelook_ecommerce`; candidate tables: `users`, `orders`, `order_items`, `products`. These names are design inputs, not a verified schema snapshot. Do not publish supposed live row counts, column types, date coverage, currency, countries, or location until inspected.

An authorized operator must capture: inspection timestamp, dataset location, exact table/column/type/nullability metadata, primary-key uniqueness evidence, foreign-key orphan counts, join cardinalities, timestamp semantics, status vocabulary and distributions, available date range, country values and their meaning, category vocabulary and missing values, numeric units/currency evidence, and table modification metadata. Store a sanitized schema snapshot and aggregate quality report under the future domain directory. Do not export raw user records. Bound and dry-run profiling queries too. Dataset metadata freshness is not proof of business-event freshness.

Disable any metric whose required field mapping or semantic assumption cannot be confirmed. Version the contract and compare schemas before live release; drift blocks affected queries until reviewed. Query in place; no copying or ingestion is specified.

## Proposed logical mappings (must be confirmed)

| Logical entity | Candidate key/fields | Grain and permitted use |
| --- | --- | --- |
| orders | order_id, user_id, status, created_at | One row per order; denominator and order eligibility |
| order_items | id, order_id, product_id, sale_price, status | One row per sold item; sales value basis |
| products | id, category, name, brand, retail_price | One row per catalog product; approved public catalog columns only |
| users | id, country | Country dimension through customer key; no names, emails, street addresses or raw user output |

Field names above are candidates, not executable mappings. Catalog `retail_price` is a list price, never realized revenue. Select an explicit display-safe column allowlist after inspection. Users/orders are available only to analyst aggregate queries, not unrestricted record browsing.

## Initial metric registry

Each registry entry stores version, capability, input schema, source lineage, output grain/unit, status/date rules, null policy and approved SQL/template version.

| ID | Proposed business definition | Conditions |
| --- | --- | --- |
| completed_item_sales | Sum item sale amount for eligible completed orders and eligible completed items | Confirm exact status values and both status mappings; exclude cancelled/returned/noncompleted rows; NOT net revenue |
| completed_orders | Distinct eligible order IDs having at least one eligible item | Same eligibility set as sales, making average consistent |
| average_completed_order_value | completed_item_sales / completed_orders | Null if denominator zero; preaggregate by order before averaging |
| catalog_product_count | Distinct product IDs within approved catalog filters | No orders or transaction join; catalog capability |
| sales_growth_pct | 100 * (current sales - prior sales) / prior sales | Two complete comparable periods; prior zero or missing yields null with reason |

No refund amounts, taxes, discounts beyond observed sale amount, shipping fees or exchange rates are presumed. Returns excluded by current status are not accounting refunds. Mutable statuses can revise historical results; label this as a current-status view. If monetary unit cannot be established, use “sale amount (currency unverified)” with no currency symbol or cross-currency total; block the monetary metric if mixed currencies cannot be resolved.

## Grain, dates and filters

Proposed date basis: order creation timestamp, grouped in explicit analysis timezone (default UTC only after timestamp semantics verification). Do not call creation-date sales cash receipts or delivery-date revenue. Date ranges are start-inclusive/end-exclusive; resolve local boundaries to timestamps before querying. Missing date range prompts clarification for time-based sales metrics. Current catalog snapshots have no date filter. Monthly report covers complete calendar months; partial periods require a visible label and are excluded from growth comparisons by default.

Country means customer profile country through the verified user join, not shipping destination or market of transaction. If unavailable or mutable, disclose limitations. Categories use verified product category. Null dimensions become a labeled Unknown group; null monetary values make the affected monetary aggregate and average null with a quality warning; status-eligible order counts remain valid. Do not publish a partial sum as complete sales or treat a missing amount as zero. A known complete calendar interval with no qualifying rows may be shown as zero; missing/failed/incomplete coverage must remain unknown. Empty filtered scope yields no_data.

Join orders to items one-to-many, items to products many-to-one and orders to users many-to-one only after cardinality checks. Use COUNT(DISTINCT order_id) for orders. Never sum order-level totals after item joins. Category counts can overlap across categories for multi-category orders and must not be summed as a grand total. Compute grand totals separately at the correct grain.

## Standard reports and custom example

- Monthly sales: completed_item_sales by month for an explicit interval, optional permitted country/category filters.
- Category ranking: sales and distinct completed orders by category; stable secondary sort by category; top N is labeled top N, not a full-population distribution.
- Country comparison: same measure/date/status semantics for a supplied country set; distinguish absent countries from zeros.
- Custom category growth: compare two explicit complete calendar periods of the same grain (for example January versus February, even though their day counts differ), or two equal-day-count custom intervals; aggregate each category separately; require `min_orders` distinct eligible orders in **each** period; return both counts, both sales and growth. Sort by growth descending, category ascending; zero baseline is unranked with an explanation. All filters precede aggregation; minimum-order thresholds follow aggregation.

Every result records contract/metric version and effective filters. Domain expansion adds verified configuration and tools; it must not weaken the shared policy gateway.

## Catalog and completeness semantics

Define standard report IDs `monthly_sales`, `category_ranking`, `country_comparison`, `catalog_product_count`, `catalog_products` and `catalog_categories`. The last three require only catalog.read and approved product columns. Catalog reports use category/brand filters, stable product/category ordering and bounded pagination; they reject date, country and sales-status fields. Catalog listing reports need no metric_id; report schemas form a discriminated union rather than one bag of optional fields. No unrestricted catalog SQL is required.

For sales comparisons record comparison_basis = calendar_period or equal_days; display both ranges. Calendar-month growth is a change in monthly totals, not a daily normalized growth measure. Reject incompatible grain/overlapping periods in v1. Resolve relative dates once per run and persist them; retries cannot move the window.

If an entire requested scope has no eligible rows, return no_data. Within an otherwise populated complete series, fill proven empty calendar buckets with zero. If eligible rows have missing amounts, return null monetary values for affected buckets, no average, and a quality warning; counts may still render. Reject duplicate source keys and unapproved join cardinality before enabling affected metrics. Missing category/user mappings use Unknown only when a reviewed left-join policy preserves base facts; never silently drop rows with an inner join.

## Definition ownership and change control

Each metric registry entry also needs a named role responsible for the definition, review state (draft/reviewed/retired), effective version, glossary/synonyms, verified source mappings, freshness expectations, allowed comparisons and known exclusions. In the demo the developer can be the declared owner; do not imply an independent finance approval. In a private pilot the customer's data steward must approve the mapping. The first public implementation must not introduce a conflicting definition called “revenue” beside the documented sale-amount measure.

Only reviewed and schema-compatible definitions are enabled for live reports. A change to status eligibility, date basis, join, null policy or currency semantics changes the metric version and invalidates incompatible caches and expected answers. Retain original provenance for historical responses; do not relabel them under a new definition. Retired/denied definitions cannot be reconstructed from old chat context.

Source modification time, max observed event time and query time are different facts. State which is available. If source freshness/completeness is unknown, do not imply the current month is finalized or that historical restatements cannot occur. Data freshness SLAs require a real data owner; this project has no ingestion pipeline or control over public dataset updates.
