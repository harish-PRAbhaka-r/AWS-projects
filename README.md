Feedback Collection System 
---
A serverless web application to collect user feedback via a static frontend and process/store it with AWS services like Lambda, DynamoDB, and SNS/SES.
---
Tech Stack
---
- HTML, JavaScript
- AWS Lambda (Python or Node.js)
- Amazon DynamoDB
- Amazon SNS / SES
- Amazon API Gateway
- Amazon S3 (for static hosting)
---
Project Structure
---
- `frontend/`: Contains static HTML + JS to collect feedback and submit to API Gateway.
- `backend/`: Contains AWS Lambda code to process and store feedback.
- `.gitignore`: Excludes AWS credentials and other sensitive files.
---
Deployment Steps
---
1. Deploy frontend to S3 (static website hosting).
2. Deploy Lambda function (can use AWS Console or SAM/Serverless Framework).
3. Create API Gateway and integrate with Lambda.
4. Connect DynamoDB and SNS/SES in Lambda.
5. Update `script.js` with your API Gateway endpoint.
---
Example Feedback Submission
---
```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "message": "Love the app!"
}
```
---
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/78c5baa1-a56d-4598-8ab2-4dd469b295c7" />
---
<img width="1000" height="1000" alt="image" src="https://github.com/user-attachments/assets/738037eb-8d55-4673-b4e6-2209cba52ecf" />
---
Security Note

❗ **Do NOT expose AWS credentials or private keys.** Use environment variables or IAM roles for secure access.
