# Database Interview Questions Collection

## SQL vs NoSQL

### Q: Explain the key differences between SQL and NoSQL databases, and give a specific scenario where you would choose one over the other.

**Answer:**
The key differences between SQL and NoSQL databases center around structure, scalability, and data integrity:

- **SQL Databases:**
  - Relational with structured schemas
  - Predefined tables and relationships
  - ACID compliant
  - Best for complex queries and transactions
  - Vertical scaling

- **NoSQL Databases:**
  - Non-relational with flexible schemas
  - Can handle unstructured data
  - Horizontal scaling
  - Better for rapid changes in data structure

**Scenario Example:**  
For an e-commerce platform:
- Use SQL (MySQL) for:
  - Order processing
  - Payment transactions
  - Inventory management
  - Customer accounts
  
- Use NoSQL (MongoDB) for:
  - Product catalog (varying attributes)
  - User sessions
  - Shopping cart data
  - Customer behavior tracking

## MongoDB Performance

### Q: How would you optimize a MongoDB query that's running slowly? Walk through your optimization process.

**Answer:**
The optimization process follows these steps:

1. **Diagnosis:**
   ```javascript
   db.collection.find({query}).explain('executionStats')
   ```
   - Analyze execution plan
   - Check number of documents scanned
   - Review current index usage

2. **Index Creation:**
   ```javascript
   db.collection.createIndex({ field1: 1 })
   ```
   - Create indexes matching query patterns
   - Consider compound indexes for multi-field queries
   - Balance index benefits against write performance

3. **Query Optimization Techniques:**
   - Use projection to limit returned fields
   - Restructure queries to leverage existing indexes
   - Ensure working set fits in memory
   - Consider query patterns and access frequency

4. **Validation:**
   ```javascript
   db.collection.aggregate([{ $indexStats: {} }])
   ```
   - Compare before/after execution times
   - Monitor index usage statistics
   - Verify memory usage
   - Check impact on write operations

## Follow-up Questions to Consider

### Redis Specific
1. What are Redis's primary use cases, and how does it differ from MongoDB?
2. Explain Redis data persistence options
3. How would you implement caching using Redis?

### PostgreSQL
1. How does PostgreSQL handle concurrency?
2. Explain MVCC in PostgreSQL
3. What are the advantages of using PostgreSQL over MySQL?

### General Database Concepts
1. Explain the CAP theorem and its implications
2. How do you handle database scaling (both vertical and horizontal)?
3. What strategies do you use for database backup and recovery?

## Best Practices for Interview Preparation

1. **Practical Experience:**
   - Prepare real-world examples from your experience
   - Be ready to discuss specific challenges you've faced
   - Have metrics ready (improvement percentages, scale of data)

2. **Technical Knowledge:**
   - Understand fundamental concepts
   - Be prepared to write pseudo-code
   - Know how to explain complex concepts simply

3. **System Design:**
   - Practice drawing architecture diagrams
   - Understand trade-offs between different solutions
   - Be ready to discuss scalability considerations

## Notes for Interviewers

- Start with fundamental concepts