from apps.core.base_models import session_maker



async def get_async_session():
    async with session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
