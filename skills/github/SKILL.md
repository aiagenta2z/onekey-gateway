---
name: github
description: Auto-generated skill for github tools via OneKey Gateway.
---

### OneKey Gateway
Use One Access Key to connect to various commercial APIs. Please visit the [OneKey Gateway Keys](https://www.deepnlp.org/workspace/keys) and read the docs [OneKey MCP Router Doc](https://www.deepnlp.org/doc/onekey_mcp_router) and [OneKey Gateway Doc](https://deepnlp.org/doc/onekey_agent_router).


# github Skill
Use the OneKey Gateway to access tools for this server via a unified access key.
## Quick Start
Set your OneKey access key:
```bash
export DEEPNLP_ONEKEY_ROUTER_ACCESS=YOUR_API_KEY
```
If no key is provided, the scripts fall back to the demo key `BETA_TEST_KEY_MARCH_2026`.
Common settings:
- `unique_id`: `github/github`
- `api_id`: one of the tools listed below
## Tools
### `add_comment_to_pending_review`
Add review comment to the requester's latest pending pull request review. A pending review needs to already exist to call this (check with the user if not sure).

Parameters:
- `body` (string, required): The text of the review comment
- `line` (number, optional): The line of the blob in the pull request diff that the comment applies to. For multi-line comments, the last line of the range
- `owner` (string, required): Repository owner
- `path` (string, required): The relative path to the file that necessitates a comment
- `pullNumber` (number, required): Pull request number
- `repo` (string, required): Repository name
- `side` (string, optional): The side of the diff to comment on. LEFT indicates the previous state, RIGHT indicates the new state Values: LEFT, RIGHT
- `startLine` (number, optional): For multi-line comments, the first line of the range that the comment applies to
- `startSide` (string, optional): For multi-line comments, the starting side of the diff that the comment applies to. LEFT indicates the previous state, RIGHT indicates the new state Values: LEFT, RIGHT
- `subjectType` (string, required): The level at which the comment is targeted Values: FILE, LINE
### `add_issue_comment`
Add a comment to a specific issue in a GitHub repository. Use this tool to add comments to pull requests as well (in this case pass pull request number as issue_number), but only if user is not asking specifically to add review comments.

Parameters:
- `body` (string, required): Comment content
- `issue_number` (number, required): Issue number to comment on
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
### `create_branch`
Create a new branch in a GitHub repository

Parameters:
- `branch` (string, required): Name for new branch
- `from_branch` (string, optional): Source branch (defaults to repo default)
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
### `create_or_update_file`
Create or update a single file in a GitHub repository. 
If updating, you should provide the SHA of the file you want to update. Use this tool to create or update a file in a GitHub repository remotely; do not use it for local file operations.

In order to obtain the SHA of original file version before updating, use the following git command:
git ls-tree HEAD <path to file>

If the SHA is not provided, the tool will attempt to acquire it by fetching the current file contents from the repository, which may lead to rewriting latest committed changes if the file has changed since last retrieval.

Parameters:
- `branch` (string, required): Branch to create/update the file in
- `content` (string, required): Content of the file
- `message` (string, required): Commit message
- `owner` (string, required): Repository owner (username or organization)
- `path` (string, required): Path where to create/update the file
- `repo` (string, required): Repository name
- `sha` (string, optional): The blob SHA of the file being replaced.
### `create_pull_request`
Create a new pull request in a GitHub repository.

Parameters:
- `base` (string, required): Branch to merge into
- `body` (string, optional): PR description
- `draft` (boolean, optional): Create as draft PR
- `head` (string, required): Branch containing changes
- `maintainer_can_modify` (boolean, optional): Allow maintainer edits
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
- `title` (string, required): PR title
### `create_repository`
Create a new GitHub repository in your account or specified organization

Parameters:
- `autoInit` (boolean, optional): Initialize with README
- `description` (string, optional): Repository description
- `name` (string, required): Repository name
- `organization` (string, optional): Organization to create the repository in (omit to create in your personal account)
- `private` (boolean, optional): Whether repo should be private
### `delete_file`
Delete a file from a GitHub repository

Parameters:
- `branch` (string, required): Branch to delete the file from
- `message` (string, required): Commit message
- `owner` (string, required): Repository owner (username or organization)
- `path` (string, required): Path to the file to delete
- `repo` (string, required): Repository name
### `fork_repository`
Fork a GitHub repository to your account or specified organization

Parameters:
- `organization` (string, optional): Organization to fork to
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
### `get_commit`
Get details for a commit from a GitHub repository

Parameters:
- `include_diff` (boolean, optional): Whether to include file diffs and stats in the response. Default is true.
- `owner` (string, required): Repository owner
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `repo` (string, required): Repository name
- `sha` (string, required): Commit SHA, branch name, or tag name
### `get_file_contents`
Get the contents of a file or directory from a GitHub repository

Parameters:
- `owner` (string, required): Repository owner (username or organization)
- `path` (string, optional): Path to file/directory
- `ref` (string, optional): Accepts optional git refs such as `refs/tags/{tag}`, `refs/heads/{branch}` or `refs/pull/{pr_number}/head`
- `repo` (string, required): Repository name
- `sha` (string, optional): Accepts optional commit SHA. If specified, it will be used instead of ref
### `get_label`
Get a specific label from a repository.

Parameters:
- `name` (string, required): Label name.
- `owner` (string, required): Repository owner (username or organization name)
- `repo` (string, required): Repository name
### `get_latest_release`
Get the latest release in a GitHub repository

Parameters:
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
### `get_me`
Get details of the authenticated GitHub user. Use this when a request is about the user's own profile for GitHub. Or when information is missing to build other tool calls.

Parameters:
- None
### `get_release_by_tag`
Get a specific release by its tag name in a GitHub repository

Parameters:
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
- `tag` (string, required): Tag name (e.g., 'v1.0.0')
### `get_tag`
Get details about a specific git tag in a GitHub repository

Parameters:
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
- `tag` (string, required): Tag name
### `get_team_members`
Get member usernames of a specific team in an organization. Limited to organizations accessible with current credentials

Parameters:
- `org` (string, required): Organization login (owner) that contains the team.
- `team_slug` (string, required): Team slug
### `get_teams`
Get details of the teams the user is a member of. Limited to organizations accessible with current credentials

Parameters:
- `user` (string, optional): Username to get teams for. If not provided, uses the authenticated user.
### `issue_read`
Get information about a specific issue in a GitHub repository.

Parameters:
- `issue_number` (number, required): The number of the issue
- `method` (string, required): The read operation to perform on a single issue.
Options are:
1. get - Get details of a specific issue.
2. get_comments - Get issue comments.
3. get_sub_issues - Get sub-issues of the issue.
4. get_labels - Get labels assigned to the issue. Values: get, get_comments, get_sub_issues, get_labels
- `owner` (string, required): The owner of the repository
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `repo` (string, required): The name of the repository
### `issue_write`
Create a new or update an existing issue in a GitHub repository.

Parameters:
- `assignees` (array of string, optional): Usernames to assign to this issue
- `body` (string, optional): Issue body content
- `duplicate_of` (number, optional): Issue number that this issue is a duplicate of. Only used when state_reason is 'duplicate'.
- `issue_number` (number, optional): Issue number to update
- `labels` (array of string, optional): Labels to apply to this issue
- `method` (string, required): Write operation to perform on a single issue.
Options are:
- 'create' - creates a new issue.
- 'update' - updates an existing issue. Values: create, update
- `milestone` (number, optional): Milestone number
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
- `state` (string, optional): New state Values: open, closed
- `state_reason` (string, optional): Reason for the state change. Ignored unless state is changed. Values: completed, not_planned, duplicate
- `title` (string, optional): Issue title
- `type` (string, optional): Type of this issue. Only use if the repository has issue types configured. Use list_issue_types tool to get valid type values for the organization. If the repository doesn't support issue types, omit this parameter.
### `list_branches`
List branches in a GitHub repository

Parameters:
- `owner` (string, required): Repository owner
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `repo` (string, required): Repository name
### `list_commits`
Get list of commits of a branch in a GitHub repository. Returns at least 30 results per page by default, but can return more if specified using the perPage parameter (up to 100).

Parameters:
- `author` (string, optional): Author username or email address to filter commits by
- `owner` (string, required): Repository owner
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `repo` (string, required): Repository name
- `sha` (string, optional): Commit SHA, branch or tag name to list commits of. If not provided, uses the default branch of the repository. If a commit SHA is provided, will list commits up to that SHA.
### `list_issue_types`
List supported issue types for repository owner (organization).

Parameters:
- `owner` (string, required): The organization owner of the repository
### `list_issues`
List issues in a GitHub repository. For pagination, use the 'endCursor' from the previous response's 'pageInfo' in the 'after' parameter.

Parameters:
- `after` (string, optional): Cursor for pagination. Use the endCursor from the previous page's PageInfo for GraphQL APIs.
- `direction` (string, optional): Order direction. If provided, the 'orderBy' also needs to be provided. Values: ASC, DESC
- `labels` (array of string, optional): Filter by labels
- `orderBy` (string, optional): Order issues by field. If provided, the 'direction' also needs to be provided. Values: CREATED_AT, UPDATED_AT, COMMENTS
- `owner` (string, required): Repository owner
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `repo` (string, required): Repository name
- `since` (string, optional): Filter by date (ISO 8601 timestamp)
- `state` (string, optional): Filter by state, by default both open and closed issues are returned when not provided Values: OPEN, CLOSED
### `list_pull_requests`
List pull requests in a GitHub repository. If the user specifies an author, then DO NOT use this tool and use the search_pull_requests tool instead.

Parameters:
- `base` (string, optional): Filter by base branch
- `direction` (string, optional): Sort direction Values: asc, desc
- `head` (string, optional): Filter by head user/org and branch
- `owner` (string, required): Repository owner
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `repo` (string, required): Repository name
- `sort` (string, optional): Sort by Values: created, updated, popularity, long-running
- `state` (string, optional): Filter by state Values: open, closed, all
### `list_releases`
List releases in a GitHub repository

Parameters:
- `owner` (string, required): Repository owner
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `repo` (string, required): Repository name
### `list_tags`
List git tags in a GitHub repository

Parameters:
- `owner` (string, required): Repository owner
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `repo` (string, required): Repository name
### `merge_pull_request`
Merge a pull request in a GitHub repository.

Parameters:
- `commit_message` (string, optional): Extra detail for merge commit
- `commit_title` (string, optional): Title for merge commit
- `merge_method` (string, optional): Merge method Values: merge, squash, rebase
- `owner` (string, required): Repository owner
- `pullNumber` (number, required): Pull request number
- `repo` (string, required): Repository name
### `pull_request_read`
Get information on a specific pull request in GitHub repository.

Parameters:
- `method` (string, required): Action to specify what pull request data needs to be retrieved from GitHub. 
Possible options: 
 1. get - Get details of a specific pull request.
 2. get_diff - Get the diff of a pull request.
 3. get_status - Get status of a head commit in a pull request. This reflects status of builds and checks.
 4. get_files - Get the list of files changed in a pull request. Use with pagination parameters to control the number of results returned.
 5. get_review_comments - Get review threads on a pull request. Each thread contains logically grouped review comments made on the same code location during pull request reviews. Returns threads with metadata (isResolved, isOutdated, isCollapsed) and their associated comments. Use cursor-based pagination (perPage, after) to control results.
 6. get_reviews - Get the reviews on a pull request. When asked for review comments, use get_review_comments method.
 7. get_comments - Get comments on a pull request. Use this if user doesn't specifically want review comments. Use with pagination parameters to control the number of results returned. Values: get, get_diff, get_status, get_files, get_review_comments, get_reviews, get_comments
- `owner` (string, required): Repository owner
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `pullNumber` (number, required): Pull request number
- `repo` (string, required): Repository name
### `pull_request_review_write`
Create and/or submit, delete review of a pull request.

Available methods:
- create: Create a new review of a pull request. If "event" parameter is provided, the review is submitted. If "event" is omitted, a pending review is created.
- submit_pending: Submit an existing pending review of a pull request. This requires that a pending review exists for the current user on the specified pull request. The "body" and "event" parameters are used when submitting the review.
- delete_pending: Delete an existing pending review of a pull request. This requires that a pending review exists for the current user on the specified pull request.

Parameters:
- `body` (string, optional): Review comment text
- `commitID` (string, optional): SHA of commit to review
- `event` (string, optional): Review action to perform. Values: APPROVE, REQUEST_CHANGES, COMMENT
- `method` (string, required): The write operation to perform on pull request review. Values: create, submit_pending, delete_pending
- `owner` (string, required): Repository owner
- `pullNumber` (number, required): Pull request number
- `repo` (string, required): Repository name
### `push_files`
Push multiple files to a GitHub repository in a single commit

Parameters:
- `branch` (string, required): Branch to push to
- `files` (array of object, required): Array of file objects to push, each object with path (string) and content (string)
- `files[].content` (string, required): file content
- `files[].path` (string, required): path to the file
- `message` (string, required): Commit message
- `owner` (string, required): Repository owner
- `repo` (string, required): Repository name
### `request_copilot_review`
Request a GitHub Copilot code review for a pull request. Use this for automated feedback on pull requests, usually before requesting a human reviewer.

Parameters:
- `owner` (string, required): Repository owner
- `pullNumber` (number, required): Pull request number
- `repo` (string, required): Repository name
### `search_code`
Fast and precise code search across ALL GitHub repositories using GitHub's native search engine. Best for finding exact symbols, functions, classes, or specific code patterns.

Parameters:
- `order` (string, optional): Sort order for results Values: asc, desc
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `query` (string, required): Search query using GitHub's powerful code search syntax. Examples: 'content:Skill language:Java org:github', 'NOT is:archived language:Python OR language:go', 'repo:github/github-mcp-server'. Supports exact matching, language filters, path filters, and more.
- `sort` (string, optional): Sort field ('indexed' only)
### `search_issues`
Search for issues in GitHub repositories using issues search syntax already scoped to is:issue

Parameters:
- `order` (string, optional): Sort order Values: asc, desc
- `owner` (string, optional): Optional repository owner. If provided with repo, only issues for this repository are listed.
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `query` (string, required): Search query using GitHub issues search syntax
- `repo` (string, optional): Optional repository name. If provided with owner, only issues for this repository are listed.
- `sort` (string, optional): Sort field by number of matches of categories, defaults to best match Values: comments, reactions, reactions-+1, reactions--1, reactions-smile, reactions-thinking_face, reactions-heart, reactions-tada, interactions, created, updated
### `search_pull_requests`
Search for pull requests in GitHub repositories using issues search syntax already scoped to is:pr

Parameters:
- `order` (string, optional): Sort order Values: asc, desc
- `owner` (string, optional): Optional repository owner. If provided with repo, only pull requests for this repository are listed.
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `query` (string, required): Search query using GitHub pull request search syntax
- `repo` (string, optional): Optional repository name. If provided with owner, only pull requests for this repository are listed.
- `sort` (string, optional): Sort field by number of matches of categories, defaults to best match Values: comments, reactions, reactions-+1, reactions--1, reactions-smile, reactions-thinking_face, reactions-heart, reactions-tada, interactions, created, updated
### `search_repositories`
Find GitHub repositories by name, description, readme, topics, or other metadata. Perfect for discovering projects, finding examples, or locating specific repositories across GitHub.

Parameters:
- `minimal_output` (boolean, optional): Return minimal repository information (default: true). When false, returns full GitHub API repository objects.
- `order` (string, optional): Sort order Values: asc, desc
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `query` (string, required): Repository search query. Examples: 'machine learning in:name stars:>1000 language:python', 'topic:react', 'user:facebook'. Supports advanced search syntax for precise filtering.
- `sort` (string, optional): Sort repositories by field, defaults to best match Values: stars, forks, help-wanted-issues, updated
### `search_users`
Find GitHub users by username, real name, or other profile information. Useful for locating developers, contributors, or team members.

Parameters:
- `order` (string, optional): Sort order Values: asc, desc
- `page` (number, optional): Page number for pagination (min 1)
- `perPage` (number, optional): Results per page for pagination (min 1, max 100)
- `query` (string, required): User search query. Examples: 'john smith', 'location:seattle', 'followers:>100'. Search is automatically scoped to type:user.
- `sort` (string, optional): Sort users by number of followers or repositories, or when the person joined GitHub. Values: followers, repositories, joined
### `sub_issue_write`
Add a sub-issue to a parent issue in a GitHub repository.

Parameters:
- `after_id` (number, optional): The ID of the sub-issue to be prioritized after (either after_id OR before_id should be specified)
- `before_id` (number, optional): The ID of the sub-issue to be prioritized before (either after_id OR before_id should be specified)
- `issue_number` (number, required): The number of the parent issue
- `method` (string, required): The action to perform on a single sub-issue
Options are:
- 'add' - add a sub-issue to a parent issue in a GitHub repository.
- 'remove' - remove a sub-issue from a parent issue in a GitHub repository.
- 'reprioritize' - change the order of sub-issues within a parent issue in a GitHub repository. Use either 'after_id' or 'before_id' to specify the new position.
- `owner` (string, required): Repository owner
- `replace_parent` (boolean, optional): When true, replaces the sub-issue's current parent issue. Use with 'add' method only.
- `repo` (string, required): Repository name
- `sub_issue_id` (number, required): The ID of the sub-issue to add. ID is not the same as issue number
### `update_pull_request`
Update an existing pull request in a GitHub repository.

Parameters:
- `base` (string, optional): New base branch name
- `body` (string, optional): New description
- `draft` (boolean, optional): Mark pull request as draft (true) or ready for review (false)
- `maintainer_can_modify` (boolean, optional): Allow maintainer edits
- `owner` (string, required): Repository owner
- `pullNumber` (number, required): Pull request number to update
- `repo` (string, required): Repository name
- `reviewers` (array of string, optional): GitHub usernames to request reviews from
- `state` (string, optional): New state Values: open, closed
- `title` (string, optional): New title
### `update_pull_request_branch`
Update the branch of a pull request with the latest changes from the base branch.

Parameters:
- `expectedHeadSha` (string, optional): The expected SHA of the pull request's HEAD ref
- `owner` (string, required): Repository owner
- `pullNumber` (number, required): Pull request number
- `repo` (string, required): Repository name

# Usage
## CLI

### add_comment_to_pending_review
```shell
onekey agent github/github add_comment_to_pending_review '{}'
```

### add_issue_comment
```shell
onekey agent github/github add_issue_comment '{}'
```

### create_branch
```shell
onekey agent github/github create_branch '{}'
```

### create_or_update_file
```shell
onekey agent github/github create_or_update_file '{}'
```

### create_pull_request
```shell
onekey agent github/github create_pull_request '{}'
```

### create_repository
```shell
onekey agent github/github create_repository '{}'
```

### delete_file
```shell
onekey agent github/github delete_file '{}'
```

### fork_repository
```shell
onekey agent github/github fork_repository '{}'
```

### get_commit
```shell
onekey agent github/github get_commit '{}'
```

### get_file_contents
```shell
onekey agent github/github get_file_contents '{}'
```

### get_label
```shell
onekey agent github/github get_label '{}'
```

### get_latest_release
```shell
onekey agent github/github get_latest_release '{}'
```

### get_me
```shell
onekey agent github/github get_me '{}'
```

### get_release_by_tag
```shell
onekey agent github/github get_release_by_tag '{}'
```

### get_tag
```shell
onekey agent github/github get_tag '{}'
```

### get_team_members
```shell
onekey agent github/github get_team_members '{}'
```

### get_teams
```shell
onekey agent github/github get_teams '{}'
```

### issue_read
```shell
onekey agent github/github issue_read '{}'
```

### issue_write
```shell
onekey agent github/github issue_write '{}'
```

### list_branches
```shell
onekey agent github/github list_branches '{}'
```

### list_commits
```shell
onekey agent github/github list_commits '{}'
```

### list_issue_types
```shell
onekey agent github/github list_issue_types '{}'
```

### list_issues
```shell
onekey agent github/github list_issues '{}'
```

### list_pull_requests
```shell
onekey agent github/github list_pull_requests '{}'
```

### list_releases
```shell
onekey agent github/github list_releases '{}'
```

### list_tags
```shell
onekey agent github/github list_tags '{}'
```

### merge_pull_request
```shell
onekey agent github/github merge_pull_request '{}'
```

### pull_request_read
```shell
onekey agent github/github pull_request_read '{}'
```

### pull_request_review_write
```shell
onekey agent github/github pull_request_review_write '{}'
```

### push_files
```shell
onekey agent github/github push_files '{}'
```

### request_copilot_review
```shell
onekey agent github/github request_copilot_review '{}'
```

### search_code
```shell
onekey agent github/github search_code '{}'
```

### search_issues
```shell
onekey agent github/github search_issues '{}'
```

### search_pull_requests
```shell
onekey agent github/github search_pull_requests '{}'
```

### search_repositories
```shell
onekey agent github/github search_repositories '{}'
```

### search_users
```shell
onekey agent github/github search_users '{}'
```

### sub_issue_write
```shell
onekey agent github/github sub_issue_write '{}'
```

### update_pull_request
```shell
onekey agent github/github update_pull_request '{}'
```

### update_pull_request_branch
```shell
onekey agent github/github update_pull_request_branch '{}'
```

## Scripts
Each tool has a dedicated script in this folder:
- `skills/github/scripts/add_comment_to_pending_review.py`
- `skills/github/scripts/add_issue_comment.py`
- `skills/github/scripts/create_branch.py`
- `skills/github/scripts/create_or_update_file.py`
- `skills/github/scripts/create_pull_request.py`
- `skills/github/scripts/create_repository.py`
- `skills/github/scripts/delete_file.py`
- `skills/github/scripts/fork_repository.py`
- `skills/github/scripts/get_commit.py`
- `skills/github/scripts/get_file_contents.py`
- `skills/github/scripts/get_label.py`
- `skills/github/scripts/get_latest_release.py`
- `skills/github/scripts/get_me.py`
- `skills/github/scripts/get_release_by_tag.py`
- `skills/github/scripts/get_tag.py`
- `skills/github/scripts/get_team_members.py`
- `skills/github/scripts/get_teams.py`
- `skills/github/scripts/issue_read.py`
- `skills/github/scripts/issue_write.py`
- `skills/github/scripts/list_branches.py`
- `skills/github/scripts/list_commits.py`
- `skills/github/scripts/list_issue_types.py`
- `skills/github/scripts/list_issues.py`
- `skills/github/scripts/list_pull_requests.py`
- `skills/github/scripts/list_releases.py`
- `skills/github/scripts/list_tags.py`
- `skills/github/scripts/merge_pull_request.py`
- `skills/github/scripts/pull_request_read.py`
- `skills/github/scripts/pull_request_review_write.py`
- `skills/github/scripts/push_files.py`
- `skills/github/scripts/request_copilot_review.py`
- `skills/github/scripts/search_code.py`
- `skills/github/scripts/search_issues.py`
- `skills/github/scripts/search_pull_requests.py`
- `skills/github/scripts/search_repositories.py`
- `skills/github/scripts/search_users.py`
- `skills/github/scripts/sub_issue_write.py`
- `skills/github/scripts/update_pull_request.py`
- `skills/github/scripts/update_pull_request_branch.py`
### Example
```bash
python3 scripts/<tool_name>.py --data '{"key": "value"}'
```

### Related DeepNLP OneKey Gateway Documents
[AI Agent Marketplace](https://www.deepnlp.org/store/ai-agent)    
[Skills Marketplace](https://www.deepnlp.org/store/skills)
[AI Agent A2Z Deployment](https://www.deepnlp.org/workspace/deploy)    
[PH AI Agent A2Z Infra](https://www.producthunt.com/products/ai-agent-a2z)    
[GitHub AI Agent Marketplace](https://github.com/aiagenta2z/ai-agent-marketplace)
## Dependencies

### CLI Dependency
Install onekey-gateway from npm
```
npm install @aiagenta2z/onekey-gateway
```

### Script Dependency
Install the required Python package before running any scripts.

```bash
pip install ai-agent-marketplace
```
Alternatively, install dependencies from the requirements file:

```bash
pip install -r requirements.txt
```
If the package is already installed, skip installation.

### Agent rule
Before executing command lines or running any script in the scripts/ directory, ensure the dependencies are installed.
Use the `onekey` CLI as the preferred method to run the skills.
