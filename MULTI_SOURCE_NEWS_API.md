# Multi-Source News API Setup Guide

# 1. Introduction
The Facebook Ad Content Verification System has been enhanced through the integration of multiple news APIs, thereby significantly improving its capacity to verify content across a diverse array of sources. Unlike systems reliant on a single provider, this multi-API approach enables concurrent querying of several reputable news sources, including NewsAPI.org, NewsData.io, TheNewsAPI.com, and WorldNewsAPI.com. Such an architecture facilitates comprehensive cross-referencing among various journalistic outlets, effectively addressing key limitations associated with single-source systems—namely rate limiting, service outages, regional coverage deficiencies, and limited content heterogeneity. By aggregating results from multiple APIs in parallel, the system not only elevates verification reliability but also extends its historical coverage back to 2018, granting access to over 100,000 global news sources spanning more than 200 countries and 89 languages. This parallel data retrieval ensures robustness, as the failure or rate limiting of one API does not impede the overall verification process.

# 2. Overview
The `newsAPI.py` script has been enhanced to support multiple news source APIs, incorporating features such as automatic fallback mechanisms and parallel query execution. This advancement allows for simultaneous querying of all enabled news providers, with their responses integrated into a cohesive data structure and accompanied by comprehensive verification results. Each news source offers distinct advantages: NewsAPI.org enables access to a broad spectrum of breaking news articles from over 50,000 sources, including a substantial free tier offering 100 requests per day; NewsData.io provides historical data starting from January 2018, encompassing more than 79,000 sources, which is particularly suited for trend analysis; TheNewsAPI.com delivers high-performance caching capabilities and supports full-text search across over one million articles weekly; and WorldNewsAPI.com offers semantic tagging, sentiment analysis, and access to an extensive network of over 6,000 newspapers worldwide. The ability to concurrently utilize multiple sources not only facilitates increased daily request limits but also broadens geographic and topical coverage, ensuring consistent verification capabilities even amidst outages or quota restrictions. The system manages source-specific data formats, error conditions, and rate limiting processes transparently, thereby providing a unified interface irrespective of the individual provider's protocol or limitations.

### 2.1 Supported News API Sources

| Source | Free Tier | Articles/Call | API Key Link | Best For |
|--------|-----------|---------------|--------------|----------|
| **NewsAPI.org** | 100 calls/day | 20 | [Get Key](https://newsapi.org) | Breaking news, 50k sources |
| **NewsData.io** | 500 calls/month | 10 | [Get Key](https://newsdata.io) | Historical data (since 2018), 79k sources |
| **TheNewsAPI.com** | Limited | 20 | [Get Key](https://thenewsapi.com) | 1M articles/week, fast caching |
| **WorldNewsAPI.com** | Limited | 20 | [Get Key](https://worldnewsapi.com) | Semantic tagging, sentiment analysis |

# 3. Configuration

The process of establishing support for multiple news source APIs entails acquiring free API keys from supported service providers and updating the `NEWS_API_SOURCES` dictionary within the `newsAPI.py` file. Each provider generally offers complimentary registration options coupled with generous usage quotas, making them well-suited for research purposes and testing scenarios. The configuration process involves visiting each provider's official website, creating an account, copying the API key from the user dashboard, and inserting it into the corresponding entry within the dictionary. Additionally, individual sources can be selectively enabled or disabled by modifying the `'enabled'` flag, thereby affording a flexible mechanism for managing which providers are queried. It is essential to activate at least one source; for applications requiring production-level performance or high-volume data processing, enabling multiple sources is advisable to leverage combined rate limits and ensure uninterrupted operation. The script is designed to automatically query all enabled sources concurrently and to aggregate the resulting data.

### 3.1 Get Your API Keys
Visit the links above and sign up for free accounts to get API keys.

### 3.2 Update newsAPI.py
Find the `NEWS_API_SOURCES` dictionary (around line 13) and add your keys:

```python
NEWS_API_SOURCES = {
    'newsapi_org': {
        'api_key': 'your_newsapi_org_key_here',
        'enabled': True,  # Set to True to enable
        'url': 'https://newsapi.org'
    },
    'newsdata_io': {
        'api_key': 'your_newsdata_io_key_here',
        'enabled': True,  # Enable after adding key
        'url': 'https://newsdata.io'
    },
    'thenewsapi': {
        'api_key': 'your_thenewsapi_key_here',
        'enabled': True,  # Enable after adding key
        'url': 'https://thenewsapi.com'
    },
    'worldnewsapi': {
        'api_key': 'your_worldnewsapi_key_here',
        'enabled': False,  # Enable after adding key
        'url': 'https://worldnewsapi.com'
    }
}
```

### 3.3 Run the Script
```bash
python newsAPI.py
```

# 4. How It Works

The multi-source news verification pipeline is designed to concurrently manage API queries from multiple news providers and effectively synthesize their results to optimize both coverage and reliability. Upon receiving a verification request, the system constructs search queries derived from extracted keywords and dispatches these queries simultaneously across all active news sources using Python's concurrent execution capabilities, thereby minimizing latency. Results obtained from each source, which often differ in format due to varying JSON schema structures, are subsequently normalized into a unified data structure known as `NewsArticle`, which encompasses standardized fields such as title, description, source, URL, and publication date. The aggregation process consolidates all retrieved articles into a single collection, preserving metadata about the originating providers to enhance transparency and facilitate validation. Importantly, the system maintains distinct instances of similar articles from different sources rather than removing duplicates; this approach supports verification through independent corroboration. For example, when multiple providers report on the same event, confidence in the authenticity of the information increases. Additionally, the system incorporates comprehensive error handling mechanisms to ensure robustness against issues such as rate limits, timeouts, or invalid responses from individual sources. Failures are logged with diagnostic warnings, but do not impede the overall process, allowing the verification operation to proceed as long as at least one source successfully responds. This fault-tolerant architecture thus ensures continuous verification performance despite potential individual provider failures.

1. **Parallel Fetching**: When you search for news, the script queries **all enabled sources** simultaneously
2. **Aggregation**: Results from all sources are combined into a single list
3. **Deduplication**: Similar articles from different sources are kept (for cross-verification)
4. **Error Handling**: If one source fails, others continue working

### 4.1 Example Output

```
Step 2: Cross-matching with News API...

Analyzing: martin-lewis-ad.webp
Content: Money Saving Expert turns attention to helping Brits...
Search keywords: money saving expert helping brits
  Searched: NewsAPI.org, NewsData.io, TheNewsAPI.com
Found 45 news articles. Analyzing similarities...
  ✓ Match found! Similarity: 78.5%
    Article: Martin Lewis warns Brits about new scam...
```

### 4.2 Rate Limit Management

#### Best Practices:
- **Start with NewsAPI.org** (100 calls/day is generous for testing)
- **Add NewsData.io** when you need more historical data
- **Enable TheNewsAPI.com** for high-volume production use
- **Monitor usage** to avoid hitting limits

#### Rotation Strategy:
Enable multiple sources and the script will use all of them, effectively multiplying your rate limits:
- NewsAPI.org: 100 calls/day
- NewsData.io: 500 calls/month (~17/day)
- TheNewsAPI.com: Variable
- **Total**: ~117+ calls/day

### 4.3 Troubleshooting

#### "No News API sources enabled!"
- Set at least one source to `'enabled': True`
- Add a valid API key for that source

#### "⚠️ NewsAPI.org error: API rate limit exceeded"
- Enable additional sources
- Wait 24 hours for rate limit reset
- Upgrade to paid plan

#### "No news articles found"
- Try different search keywords
- Check if your query is too specific
- Verify API keys are valid

### 4.4 Advanced: Source-Specific Features

#### NewsData.io
- Access to historical data from Jan 2018
- 206 countries, 89 languages
- Good for trend analysis

#### WorldNewsAPI.com
- **Semantic tagging** (locations, organizations, persons)
- **Sentiment analysis** (English & German only)
- Front pages from 6,000+ newspapers

#### TheNewsAPI.com
- **Full-text search** in article content
- Fast caching technology
- Good for real-time feeds

### 4.5 Cost Comparison (If You Outgrow Free Tiers)

| Source | Paid Plan | Articles/Month |
|--------|-----------|----------------|
| NewsAPI.org | $449/mo | 250,000 |
| NewsData.io | $199/mo | 100,000 |
| TheNewsAPI.com | Contact | Custom |
| WorldNewsAPI.com | Contact | Custom |

### 4.6 Migration from Single Source

If you're currently using the old single-source code:
1. Your existing `NEWS_API_KEY` still works (mapped to `newsapi_org`)
2. No code changes needed in other parts of your script
3. Just add more sources when ready

### 4.7 Next Steps

1. Get free API keys from 2-3 sources
2. Enable them in `NEWS_API_SOURCES`
3. Run `python newsAPI.py` to test
4. Monitor your usage on each provider's dashboard
5. Scale up by enabling more sources as needed

# 5. Summary
The integration of a multi-source news API represents a significant advancement in the development of the Facebook Ad Content Verification System, transitioning it from a monocular data source to a comprehensive, high-coverage verification platform. This system facilitates concurrent queries across multiple news data providers, including NewsAPI.org, NewsData.io, TheNewsAPI.com, and WorldNewsAPI.com, thereby enhancing operational capacity through increased rate limits—over 117 requests per day within free tiers—and expanding both geographic and topical coverage to encompass over 100,000 global sources. Additionally, it provides access to extensive historical data dating back to 2018, supporting longitudinal analyses. The robustness of the system is further reinforced by an automatic failover mechanism that ensures continuity during provider outages or quota restrictions. Its user interface abstracts provider-specific complexities while maintaining source attribution transparency, thereby supporting both automated workflows and manual validation processes. This architecture is particularly advantageous for academic research requiring extensive datasets, real-time misinformation detection necessitating high availability, and policy analysis that benefits from diverse journalistic perspectives. The capacity to selectively enable or disable individual sources allows users to tailor the system according to specific analytical needs—such as semantic analysis, historical data retrieval, or live news monitoring. When combined with existing OCR extraction and similarity matching functionalities, this multi-source API integration significantly enhances the system's capacity to combat digital misinformation, positioning it as a versatile and powerful tool for scholarly and applied research in media verification.