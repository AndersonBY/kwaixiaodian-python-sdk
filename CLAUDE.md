# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a comprehensive Python SDK for the Kuaishou (快手小店) e-commerce platform open API. It's a modern async-first SDK that provides complete integration capabilities with Kuaishou's merchant platform, covering 25+ business domains and 500+ API endpoints including orders, products, refunds, logistics, payments, and OAuth authentication.

## Development Commands

The project uses PDM (Python Dependency Management) for dependency management and scripts:

```bash
# Install dependencies
pdm install

# Code formatting and linting
pdm run format        # Format code with ruff
pdm run lint          # Lint code with ruff
pdm run typecheck     # Type check with pyright

# Testing
pdm run test          # Run full test suite with coverage
pdm run test-fast     # Quick test run (exit on first failure)

# Documentation
pdm run docs          # Serve docs locally
pdm run build-docs    # Build documentation

# Quality checks
pdm run pre-commit    # Run all pre-commit hooks
pdm run clean         # Clean build artifacts
```

## Architecture Overview

### Core Structure
- **`src/kwaixiaodian/`** - Main SDK package
- **`client/main.py`** - Primary `AsyncKwaixiaodianClient` and `SyncKwaixiaodianClient` classes
- **`client/oauth.py`** - `OAuthClient` for authentication flows
- **`client/base.py`** - `AsyncBaseClient` and `SyncBaseClient` for shared HTTP communication
- **`client/services/`** - 25+ business service implementations covering all API domains

### Supported Services
**Core Business Services:**
- **Order Management** - Order lifecycle, logistics, merchant operations
- **Item Management** - Product catalog, inventory, size charts, videos  
- **Refund Management** - Return processing, dispute handling
- **Logistics** - Shipping, express templates, delivery tracking
- **Financial Services** - Bills, payments, deposits, invoicing

**Platform Services:**
- **Customer Service** - AI messaging, group dispatching, callbacks
- **Dropshipping** - Supply chain, order allocation, merchant relations
- **SCM** - Warehouse management, inventory control
- **SMS** - Messaging, templates, delivery tracking
- **Live Streaming** - Broadcast management, interaction tools

**Specialized Services:**
- **Industry** - Virtual goods, secondhand marketplace
- **Service Market** - Service orders, buyer management  
- **Local Life** - Location-based services, order management
- **Supply Chain** - Item synchronization, supplier integration
- **Comment Management** - Reviews, moderation, analytics

### Key Design Patterns
- **Async-first with Sync Support**: All services available in both async and sync versions
- **Service-oriented**: Business logic separated into domain-specific service classes
- **Type-safe**: Full Pydantic v2 integration for request/response validation
- **Error handling**: Comprehensive exception hierarchy with specific error types

### Authentication
- OAuth 2.0 flow with automatic token refresh
- HMAC-SHA256/MD5 signature verification
- Configurable retry logic for authentication failures

### Models and Services
- **Models** (`models/`) - 500+ Pydantic data models for API requests/responses
- **Services** (`client/services/`) - Business logic implementations for 25+ domains
- **HTTP layer** (`http/`) - Async/sync HTTP client with connection pooling
- **Auth layer** (`auth/`) - OAuth and signature handling

## Python Environment
- **Python version**: 3.8+ (supports 3.8-3.12)
- **Async framework**: Built on `httpx` for HTTP, `asyncio` for concurrency
- **Validation**: Pydantic v2 for data models and validation
- **JSON**: `orjson` for high-performance JSON processing

## Testing Approach
- Test files in `tests/` directory
- Uses `pytest` with async support (`pytest-asyncio`)
- Coverage reporting with 90%+ target coverage
- Mock HTTP responses with `respx` library

## Code Quality Tools
- **Ruff**: Linting and formatting (replaces black, isort, flake8)
- **Pyright**: Static type checking in strict mode
- **Pre-commit**: Automated quality checks on commit
- **Coverage**: Code coverage tracking with htmlcov reports

## Development Principles
- **Java SDK Reference**: All APIs strictly based on official Java SDK implementations
- **No Speculative APIs**: Only implement APIs that exist in the Java SDK reference
- **Comprehensive Coverage**: Support for both async and sync programming models
- **Enterprise Ready**: Production-ready with full error handling and retry logic

## Important Notes
- SDK supports both async (`AsyncKwaixiaodianClient`) and sync (`SyncKwaixiaodianClient`) clients
- Use context managers (`async with client:` or `with client:`) for proper resource cleanup
- Token management is automatic but requires proper OAuth setup
- All monetary values are handled in smallest currency units (分/cents)
- The project follows semantic versioning
- Extensive documentation and examples available for all services