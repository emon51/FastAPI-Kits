# FastAPI-Kits

## If we get an error while to activate virtualenv
- When we type: ``` ... myenv\Scripts\activate ``` 
**Error:**
...\myenv\Scripts\activate cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170. At line:1 char:1 + myenv/Scripts/activate + CategoryInfo : SecurityError: (:) [], PSSecurityException + FullyQualifiedErrorId : UnauthorizedAccess

- Solution: ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser```
