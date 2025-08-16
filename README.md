Feedback Collection System 
<hr>
A serverless web application to collect user feedback via a static frontend and process/store it with AWS services like Lambda, DynamoDB, and SNS/SES.
<hr>
Tech Stack
<hr>
- HTML, JavaScript
- AWS Lambda (Python or Node.js)
- Amazon DynamoDB
- Amazon SNS / SES
- Amazon API Gateway
- Amazon S3 (for static hosting)
<hr>
Project Structure
<hr>
- `frontend/`: Contains static HTML + JS to collect feedback and submit to API Gateway.
- `backend/`: Contains AWS Lambda code to process and store feedback.
- `.gitignore`: Excludes AWS credentials and other sensitive files.
<hr>
Deployment Steps
<hr>
1. Deploy frontend to S3 (static website hosting).
2. Deploy Lambda function (can use AWS Console or SAM/Serverless Framework).
3. Create API Gateway and integrate with Lambda.
4. Connect DynamoDB and SNS/SES in Lambda.
5. Update `script.js` with your API Gateway endpoint.
<hr>
Example Feedback Submission

```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "message": "Love the app!"
}
```
<hr>
<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/78c5baa1-a56d-4598-8ab2-4dd469b295c7" />
<hr>
<img width="1899" height="801" alt="image" src="https://github.com/user-attachments/assets/738037eb-8d55-4673-b4e6-2209cba52ecf" />

<hr>
Security Note

❗ **Do NOT expose AWS credentials or private keys.** Use environment variables or IAM roles for secure access.
